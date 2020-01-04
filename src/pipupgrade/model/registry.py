# imports - standard imports
import re
from   functools import partial

# imports - module imports
from pipupgrade.model.package   import Package, _get_pip_info
from pipupgrade                 import _pip, parallel
from pipupgrade.util.types      import flatten
from pipupgrade.util.array      import compact
from pipupgrade.util.string     import kebab_case, lower
from pipupgrade._compat		    import iteritems, iterkeys, itervalues
from pipupgrade.tree            import Node as TreeNode
from pipupgrade.log             import get_logger

logger = get_logger()

# cache package information
_INFO_DICT = dict()
# cache dependency trees
_TREE_DICT = dict()

def _build_packages_info_dict(packages, pip_exec = None):
    details         = _get_pip_info(*packages, pip_exec = pip_exec)

    requirements    = [ ]

    for name, detail in iteritems(details):
        if not name in _INFO_DICT:
            _INFO_DICT[name] = dict({
                     "version": detail["version"], 
                "dependencies": compact(
                    map(lower, detail["requires"].split(", "))
                )
            })

            for requirement in _INFO_DICT[name]["dependencies"]:
                if requirement not in requirements:
                    requirements.append(requirement)

    if requirements:
        _build_packages_info_dict(requirements, pip_exec = pip_exec)

def _create_package(name, sync = False):
    package                 = Package(name, sync = sync)
    package.current_version = _INFO_DICT[name]["version"]
    
    return package

def _get_dependency_tree_for_package(package, parent = None, sync = False,
    jobs = 1):
    if package.name not in _TREE_DICT:
        logger.info("Building dependency tree for package: %s..." % package)

        tree            = TreeNode(package, parent = parent)

        dependencies    = [ ]
        
        with parallel.no_daemon_pool(processes = jobs) as pool:
            dependencies = pool.map(
                partial(
                    _create_package, **{
                        "sync": sync
                    }
                ),
                _INFO_DICT[package.name]["dependencies"]
            )

        with parallel.no_daemon_pool(processes = jobs) as pool:
            children = pool.map(
                partial(
                    _get_dependency_tree_for_package, **{
                        "parent": tree
                    }
                ),
                dependencies
            )

            if children:
                tree.add_children(*children)

        _TREE_DICT[package.name] = tree
    else:
        logger.info("Using cached dependency tree for package: %s." % package)

    tree        = _TREE_DICT[package.name]
    tree.parent = parent

    return tree

class Registry:
    def __init__(self,
        source,
        packages                = [ ],
        installed               = False,
        sync                    = False,
        build_dependency_tree   = False,
        jobs                    = 1
    ):
        self.source = source

        args        = { "sync": sync }

        if installed:
            args["pip_exec"] = source
        
        with parallel.no_daemon_pool(processes = jobs) as pool:
            self.packages = pool.map(partial(Package, **args), packages)

        self.installed = installed
        
        if installed and build_dependency_tree and self.packages:
            self._build_dependency_tree_for_packages(sync = sync, jobs = jobs)

    def _build_dependency_tree_for_packages(self, sync = False, jobs = 1):
        names = [p.name for p in self.packages]
        _build_packages_info_dict(names, pip_exec = self.source)

        for package in self.packages:
            package.dependency_tree = _get_dependency_tree_for_package(package,
                sync = sync, jobs = 1)
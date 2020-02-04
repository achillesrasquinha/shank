from shank.model.package import (
    _get_pypi_info,
    _get_package_version,
    _get_pip_info
)
from shank.__attr__ import (
    __name__    as NAME,
    __author__
)
from shank import semver

def test___get_pypi_info():
    info = _get_pypi_info("shank")
    assert info["author"] == "Achilles Rasquinha"

def test__get_package_version():
    version = _get_package_version("shank")
    semver.parse(version)

def test__get_pip_info():
    packages = _get_pip_info("shank", "pytest")

    assert packages["shank"]["name"]      == NAME
    assert packages["shank"]["author"]    == __author__

    assert packages["pytest"]["name"]          == "pytest"
    assert packages["pytest"]["license"]       == "MIT license"
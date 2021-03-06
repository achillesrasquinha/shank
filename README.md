<div align="center">
  <img src=".github/assets/meme.jpg">
  <h1>
    shank
  </h1>
  <h4>A Python Popen that does not suck.</h4>
</div>

<p align="center">
    <a href="https://travis-ci.org/achillesrasquinha/shank">
        <img src="https://img.shields.io/travis/achillesrasquinha/shank.svg?style=flat-square">
    </a>
    <a href="https://ci.appveyor.com/project/achillesrasquinha/shank">
        <img src="https://img.shields.io/appveyor/ci/achillesrasquinha/shank.svg?style=flat-square&logo=appveyor">
    </a>
    <a href="https://coveralls.io/github/achillesrasquinha/shank">
        <img src="https://img.shields.io/coveralls/github/achillesrasquinha/shank.svg?style=flat-square">
    </a>
    <a href="https://pypi.org/project/shank/">
		<img src="https://img.shields.io/pypi/v/shank.svg?style=flat-square">
	</a>
    <a href="https://pypi.org/project/shank/">
		<img src="https://img.shields.io/pypi/l/shank.svg?style=flat-square">
	</a>
    <a href="https://pypi.org/project/shank/">
		<img src="https://img.shields.io/pypi/pyversions/shank.svg?style=flat-square">
	</a>
    <a href="https://hub.docker.com/r/achillesrasquinha/shank">
		<img src="https://img.shields.io/docker/cloud/build/achillesrasquinha/shank.svg?style=flat-square&logo=docker">
	</a>
    <a href="https://git.io/boilpy">
      <img src="https://img.shields.io/badge/made%20with-boilpy-red.svg?style=flat-square">
    </a>
	<a href="https://saythanks.io/to/achillesrasquinha">
		<img src="https://img.shields.io/badge/Say%20Thanks-🦉-1EAEDB.svg?style=flat-square">
	</a>
	<a href="https://paypal.me/achillesrasquinha">
		<img src="https://img.shields.io/badge/donate-💵-f44336.svg?style=flat-square">
	</a>
</p>

<div align="center">
  <img src=".github/assets/demo.gif">
</div>

### Table of Contents
* [Features](#Features)
* [Installation](#installation)
* [Usage](#usage)
  * [Basic Usage](#basic-usage)
  * [Docker](#docker)
  * [Environment Variables](docs/source/envvar.md)
* [FAQ](FAQ.md)
* [License](#license)

### Features
* Updates system packages and local packages.
* Discovers packages present within multiple Python Environments.
* Updates packages mentioned within a `requirements.txt` file (Also pins up-to-date versions if mentioned).
* Smart `requirements.txt` detector.
* [Pipfile](https://github.com/pypa/pipenv) support.
* Detects semantic version to avoid updates that break changes. **Also ensures to avoid
 child dependencies that break changes.**
* [View Dependency Graph.](FAQ.md/#how-do-i-view-a-dependency-graph)
* Parallel updates (blazingly fast).
* Python 2.7+ and Python 3.4+ compatible. Also pip 9+, pip 10+, pip 18+ and [pip 19.0.1+](https://github.com/pypa/pip/issues/6158) compatible.
* Automate your Dependencies by installing `shank` in your CI workflow.
* Zero Dependencies!

### Installation

```shell
$ pip install shank
```

### Usage

#### Basic Usage

* [**`shank`**](https://git.io/shank)

*Upgrades all the packages across all detected pip environments.*

* [**`shank --self`**](https://git.io/shank)

*Upgrades `shank`.*

* [**`shank --format {table,tree,json,yaml}`**](https://git.io/shank)

*Display packages in the format (defaults to `table`)*

* [**`shank --pip-path PIP_PATH`**](https://git.io/shank)

*Upgrades all the packages within the defined pip environment.*

* [**`shank --check`**](https://git.io/shank)

*Checks and pretty prints outdated packages (Does not perform upgrades).*

* [**`shank --latest`**](https://git.io/shank)

*WARNING: Upgrades all packages (including the ones that break change).*

* [**`shank --all`**](https://git.io/shank)

*List all packages.*

* [**`shank --interactive`**](https://git.io/shank)

*Prompts confirmation dialog for each package to be upgraded.*

* [**`shank --requirements REQUIREMENTS`**](https://git.io/shank)

*Upgrades the requirements file (if required).*

* [**`shank --pipfile PIPFILE`**](https://git.io/shank)

*Upgrades the Pipfile and Pipfile.lock file (if required).*

* [**`shank --project PROJECT`**](https://git.io/shank)

*Upgrades all the requirements file and/or Pipfile/Pipfile.lock within a project directory.*

That's basically it! Run the help for more details...

```
$ shank --help
usage: shank [--pip-path PIP_PATH] [-y] [-c] [-l]
                  [-f {table,tree,json,yaml}] [-a] [--pip] [-s]
                  [-r REQUIREMENTS] [--pipfile PIPFILE] [-i] [-p PROJECT]
                  [--git-username GIT_USERNAME] [--git-email GIT_EMAIL]
                  [--pull-request] [--github-access-token GITHUB_ACCESS_TOKEN]
                  [--github-reponame GITHUB_REPONAME]
                  [--github-username GITHUB_USERNAME]
                  [--target-branch TARGET_BRANCH] [-j JOBS] [-u]
                  [--no-included-requirements] [--no-cache] [-o OUTPUT]
                  [--force] [--no-color] [-V] [-v] [-h]
                  [packages [packages ...]]

shank (v 1.6.6)

UPGRADE ALL THE PIP PACKAGES!

positional arguments:
  packages              Packages to Upgrade. (default: None)

optional arguments:
  --pip-path PIP_PATH   Path to pip executable to be used. (default: None)
  -y, --yes             Confirm for all dialogs. (default: 0)
  -c, --check           Perform a dry-run, avoid updating packages. (default:
                        0)
  -l, --latest          Update all packages to latest. (default: 0)
  -f {table,tree,json,yaml}, --format {table,tree,json,yaml}
                        Display packages format. (default: table)
  -a, --all             List all packages. (default: 0)
  --pip                 Update pip. (default: 0)
  -s, --self            Update shank. (default: False)
  -r REQUIREMENTS, --requirements REQUIREMENTS
                        Path(s) to requirements.txt file. (default: None)
  --pipfile PIPFILE     Path(s) to Pipfile (default: None)
  -i, --interactive     Interactive Mode. (default: 0)
  -p PROJECT, --project PROJECT
                        Path(s) to Project (default: None)
  --git-username GIT_USERNAME
                        Git Username (default: None)
  --git-email GIT_EMAIL
                        Git Email (default: None)
  --pull-request        Perform a Pull Request. (default: False)
  --github-access-token GITHUB_ACCESS_TOKEN
                        GitHub Access Token (default: None)
  --github-reponame GITHUB_REPONAME
                        Target GitHub Repository Name (default: None)
  --github-username GITHUB_USERNAME
                        Target GitHub Username (default: None)
  --target-branch TARGET_BRANCH
                        Target Branch (default: master)
  -j JOBS, --jobs JOBS  Number of Jobs to be used. (default: 4)
  -u, --user            Install to the Python user install directory for
                        environment variables and user configuration.
                        (default: 0)
  --no-included-requirements
                        Avoid updating included requirements. (default: 0)
  --no-cache            Avoid fetching latest updates from PyPI server.
                        (default: 0)
  -o OUTPUT, --output OUTPUT
                        Print Output to File. (default: None)
  --ignore-error        Ignore Error in case of upgrade failure. (default: 0)
  --force               Force search for files within a project. (default: 0)
  --no-color            Avoid colored output. (default: 0)
  -V, --verbose         Display verbose output. (default: False)
  -v, --version         Show shank's version number and exit.
  -h, --help            Show this help message and exit.
```

### Docker

Using `shank`'s Docker Image to generate a Pull Request can be done as follows:

```
$ docker run \
    -e "shank_GIT_USERNAME=<YOUR_GIT_USERNAME>" \
    -e "shank_GIT_EMAIL=<YOUR_GIT_EMAIL>" \
    -e "shank_GITHUB_REPONAME=<YOUR_GIT_REPONAME>" \
    -e "shank_GITHUB_USERNAME=<YOUR_GIT_USERNAME>" \
    --rm \
    -it \
    -v $(pwd):/path/to/project \
      achillesrasquinha/shank \
        --project /path/to/project \
        --pull-request \
        --force \
        --yes \
        --verbose
```

### Similar Packages

`shank` attempts to provide an all-in-one solution as compared to the following packages:

* [pur](https://github.com/alanhamlett/pip-update-requirements)
* [pip_upgrade_outdated](https://github.com/defjaf/pip_upgrade_outdated)
* [pipdate](https://github.com/nschloe/pipdate)
* [pip-review](https://github.com/jgonggrijp/pip-review)
* [pip-upgrader](https://github.com/simion/pip-upgrader)

### License

This repository has been released under the [MIT License](LICENSE).

---

<div align="center">
  Made with ❤️ using <a href="https://git.io/boilpy">boilpy</a>.
</div>

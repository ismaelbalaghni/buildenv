# buildenv
Build environment setup system, based on Python venv

<!-- NMK-BADGES-BEGIN -->
[![License: MPL](https://img.shields.io/github/license/ismaelbalaghni/buildenv?color=green)](https://github.com/ismaelbalaghni/buildenv/blob/main/LICENSE)
[![Checks](https://img.shields.io/github/actions/workflow/status/ismaelbalaghni/buildenv/build.yml?branch=main&label=build%20%26%20u.t.)](https://github.com/ismaelbalaghni/buildenv/actions?query=branch%3Amain)
[![Issues](https://img.shields.io/github/issues-search/ismaelbalaghni/buildenv?label=issues&query=is%3Aopen+is%3Aissue)](https://github.com/ismaelbalaghni/buildenv/issues?q=is%3Aopen+is%3Aissue)
[![Supported python versions](https://img.shields.io/badge/python-3.9%20--%203.12-blue)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/buildenv)](https://pypi.org/project/buildenv/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://astral.sh/ruff)
[![Ruff analysis result](https://img.shields.io/badge/ruff-0-green)](https://astral.sh/ruff)
[![Code coverage](https://img.shields.io/codecov/c/github/ismaelbalaghni/buildenv)](https://app.codecov.io/gh/ismaelbalaghni/buildenv)
[![Documentation Status](https://readthedocs.org/projects/buildenv/badge/?version=stable)](https://buildenv.readthedocs.io/)
<!-- NMK-BADGES-END -->

## Features

The **`buildenv`** tool provides following features:
* simple build environment setup through loading scripts generated in your project
* configuration through a simple **`buildenv.cfg`** file
* extendable activation scripts, loaded with the build environment

The full **`buildenv`** documentation is available at [https://buildenv.readthedocs.io](https://buildenv.readthedocs.io)

## Local build

If you want to build locally the **`buildenv`** wheel, just:
1. clone the **`buildenv`** project
1. launch the loading script (see above)
1. build the project: `nmk build`

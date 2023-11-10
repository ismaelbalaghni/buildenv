# Features

The purpose of the **`buildenv`** tool is to help projects to setup easily a build environment, just after clone, with minimal dependencies (i.e. only [**git**](https://git-scm.com/) and [**python**](https://www.python.org/)).

## "loadme" scripts

The main feature of the **`buildenv`** tool is to generate "**loadme**" scripts in the project root folder, ready to be executed just after the project is cloned, and loading everything so that the project is ready to build (whatever is the used build system).

In other words, the typical project setup scenario with **`buildenv`** is:
1. clone the project -- `git clone git@github.com:xxx/yyy.git`
1. launch the **loadme** script:
    * on Linux: `source loadme.sh`
    * on Windows: `loadme.cmd`
1. build the project

# Irnas Bluepie Software

This repository contains often used BLE wrappers around [bleak](https://github.com/hbldh/bleak).

## Installation and updating
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Toolbox like below.
Rerun this command to check for and install  updates.
```bash
pip install git+https://github.com/IRNAS/irnas-bluepie-software
```

To download exact tagged version of this package add below line in `requirements.txt` file which is passed to `pip install --requirements requirements.txt`
```text
git+https://github.com/IRNAS/irnas-bluepie-software.git@<tag_version>
```

## Developing

For development and testing the use of `virtualenv` is suggested.

Install `virtualenv`:
```bash
pip install virtualenv
```

Create and activate `virtualenv`, run this from project root:

```bash
virtualenv venv
. /venv/bin/activate
```

To make development of the python package more smooth you can run below command from the project root directory.
Changes that you make in the source code will be automatically available instead of running `pip install .` all time.
```bash
pip install --editable .
```

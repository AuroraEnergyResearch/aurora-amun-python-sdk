# Aurora Amun SDK

## This is under development and not for general use.

## Developing

### Create a venv and activate if required

```powershell
python -m venv .venv
#enable python virtual environment
.\.venv\Scripts\Activate.ps1
```

### Install dependencies

```powershell
# This install this module as symlinks to and all dependencies including the ones needed locally.
# It uses setup.py to find dependancies.
pip install -e  .[development] # This install this module as symlinks to and all dependencies including the ones needed locally.
```

### Building the documentation

```powershell
.\.venv\Scripts\Activate.ps1
pydoc-markdown
```

This expected the documentation [aurora-amun-python-sdk-docs](https://auroraenergyresearch.github.io/aurora-amun-python-sdk-docs/) to be checked out as a sibling in `..\aurora-amun-python-sdk-docs\`

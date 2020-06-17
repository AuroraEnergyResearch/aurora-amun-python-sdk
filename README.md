# Aurora Amun SDK

## This is under development and not for general use.

## Installing

```powershell
pip install git+https://github.com/AuroraEnergyResearch/aurora-amun-python-sdk
```

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

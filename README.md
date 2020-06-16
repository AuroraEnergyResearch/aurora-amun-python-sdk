# Aurora Amun SDK

## Installing

```
pip install git+https://github.com/AuroraEnergyResearch/aurora_amun_python_sdk
```

## Developing

1. Create a venv and activate if required

```powershell
python -m venv .venv
#enable python virtual environment
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies

```powershell
# This install this module as symlinks to and all dependencies including the ones needed locally.
# It uses setup.py to find dependancies.
pip install -e  .[development] # This install this module as symlinks to and all dependencies including the ones needed locally.
```

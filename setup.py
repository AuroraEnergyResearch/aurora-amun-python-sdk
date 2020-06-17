from setuptools import setup

setup(
    name="aurora-amun-sdk",
    version="0.1.2",
    description="",
    url="https://github.com/AuroraEnergyResearch/aurora-amun-python-sdk",
    author="Gareth Rylance",
    author_email="gareth@rylance.me.uk",
    packages=["aurora.amun"],
    install_requires=["requests"],
    zip_safe=False,
    entry_points={"console_scripts": [""]},
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    extras_require={"development": ["flake8", "black", "pytest", "snapshottest"]},
)

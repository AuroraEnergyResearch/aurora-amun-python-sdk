from setuptools import setup

setup(
    name="aurora_amun_sdk",
    version="0.1",
    description="The dispatch model loader - lambda part.",
    url="https://github.com/AuroraEnergyResearch/aurora_amun_python_sdk",
    author="Gareth Rylance",
    author_email="gareth@rylance.me.uk",
    packages=["aurora_amun_sdk"],
    install_requires=[],
    zip_safe=False,
    entry_points={"console_scripts": [""]},
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    extras_require={"development": ["flake8", "black", "pytest", "snapshottest"]},
)

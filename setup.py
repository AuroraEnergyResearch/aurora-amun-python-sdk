from setuptools import setup

setup(
    name="aurora-amun-sdk",
    version="1.0.0",
    description="",
    url="https://github.com/AuroraEnergyResearch/aurora-amun-python-sdk",
    author="Aurora Development team",
    author_email="aurora_development@auroraer.com",
    packages=["aurora.amun.client"],
    install_requires=["requests"],
    zip_safe=False,
    entry_points={"console_scripts": [""]},
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    extras_require={
        "development": ["flake8", "black", "pytest", "snapshottest", "novella", "pydoc-markdown[novella]"],
        "notebooks": ["matplotlib", "pandas", "ipykernel"],
    },
)
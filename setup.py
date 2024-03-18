from setuptools import setup

setup(
    name='physicalunits',
    version='0.0.2',
    install_requires=[
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3, <4",
    project_urls={  # Optional
        "Bug Reports": "https://github.com/jeffcodez/PhysicalUnits/issues",
        "Source": "https://github.com/jeffcodez/PhysicalUnits",
    },
)
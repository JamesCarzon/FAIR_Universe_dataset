# setup.py
from setuptools import setup, find_packages

setup(
    name="hep_challenge",
    version="0.1",
    packages=find_packages(where="."),
    package_dir={"": "."},
)

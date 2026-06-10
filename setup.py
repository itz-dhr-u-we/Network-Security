# this file is used to install the package using pip. to define configuration,such as its metadata,dependencies and more.
from setuptools import find_packages, setup
#find_packages discovers __init__.py files and includes those directories as packages in the distribution.
#setup() is the main function used to define the package's metadata, dependencies, and other configuration options.
from typing import List

def get_requirements()->List[str]:
    """
    This function reads the requirements.txt file and returns a list of dependencies required for the package.
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # read all lines from file
            for line in file:
                requirement = line.strip()
                # ignores empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please make sure it exists in the same directory as setup.py.")
    return requirement_lst

setup(
    name = "NetworkSecurity",
    version="0.0.1",
    author="Dhruvi Ladvaiya",
    packages=find_packages(),
    install_requires=get_requirements()
)
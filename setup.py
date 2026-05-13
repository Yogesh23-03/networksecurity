"""
The setup.py file is a core part of Python packaging and distribution.

It is used by the setuptools library to define how your Python project
should be packaged, installed, and distributed to other systems.

With setup.py, you can specify:

1. Project metadata
   - name of the package
   - version number
   - author name and email
   - project description
   - license information

2. Dependencies
   - external libraries required for the project to run
   - these are automatically installed when the package is installed

3. Package structure
   - which Python packages and modules should be included

4. Entry points
   - command-line commands that users can run directly after installation

5. Additional files
   - README, configuration files, datasets, templates, etc.

6. Python version requirements
   - minimum and maximum supported Python versions

Common usage:
    python setup.py install
    pip install .
    pip install -e .

What does "-e ." mean?
    -e stands for "editable mode".
    In editable mode, any changes made to your source code are immediately
    reflected without reinstalling the package.

Why is setup.py important?
    - Converts your project into a reusable Python package
    - Makes imports work cleanly across the project
    - Simplifies dependency management
    - Enables publishing to PyPI (Python Package Index)
    - Used extensively in professional and production-grade projects

Example:
    from setuptools import setup, find_packages

    setup(
        name="my_project",
        version="0.1.0",
        author="Yogesh",
        packages=find_packages(),
        install_requires=[
            "numpy",
            "pandas",
            "scikit-learn"
        ]
    )

In modern Python projects, pyproject.toml is becoming the preferred
configuration file, but setup.py is still widely used and remains
important to understand, especially in machine learning and MLOps projects.

In your ML project, setup.py is often used together with:
    - requirements.txt  -> lists dependencies
    - src/              -> contains source code
    - pip install -e .  -> installs your project as a package

This allows imports such as:
    from src.pipeline.train_pipeline import TrainPipeline

instead of relying on manually changing Python paths.
"""
from setuptools import setup, find_packages
from typing import List


def get_requirements() -> List[str]:
    """
    Reads the requirements.txt file and returns a list of dependencies.
    Removes '-e .' because it is used only for editable installation.
    """
    requirements_list: List[str] = []

    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            # Remove leading and trailing spaces/newlines
            requirement = line.strip()

            # Ignore empty lines and '-e .'
            if requirement and requirement != "-e .":
                requirements_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found.")
        print("Please ensure it exists in the project root.")
        print("You can create it using: pip freeze > requirements.txt")

    return requirements_list


setup(
    name="networksecurity2",
    version="0.1.0",
    author="Yogesh",
    packages=find_packages(),
    install_requires=get_requirements(),
    description="A machine learning project for network security.",
    author_email="s66909287@gmail.com",
)
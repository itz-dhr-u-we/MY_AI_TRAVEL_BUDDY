from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
   
    # the above lines of code are for the setup.py file, which is used to specify the dependencies for the project. It reads the requirements from the requirements.txt file and uses them in the setup function to install the necessary packages when the project is installed.

    setup(
        name="My AI Travel Buddy",
        version="0.1",
        install_requires=requirements, 
        author="Dhruvi Ladvaiya",
        packages=find_packages()
    )
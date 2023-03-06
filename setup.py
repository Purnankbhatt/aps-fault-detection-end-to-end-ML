from setuptools import find_packages,setup

setup(
    name = "sensor",
    version="0.0.1",
    author="ineuron",
    author_email = "purnankbhatt4191@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)
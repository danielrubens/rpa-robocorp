from setuptools import setup, find_packages

setup(
    name="rpa_robocorp",
    description="RPA Robocorp",
    install_requires=[
        "requests==2.3.0",
        "python-decouple==3.3",
    ],
    packages=find_packages(exclude=['tests']),
)
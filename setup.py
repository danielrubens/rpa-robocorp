from setuptools import setup

setup(
    name="rpa_robocorp",
    description="RPA Robocorp",
    install_requires=[
        "parsel==1.7.0",
        "requests==2.24.0",
        "python-decouple==3.3",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
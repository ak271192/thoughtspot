from setuptools import find_packages, setup

setup(
    name="dagster_pipeline1",
    packages=find_packages(exclude=["dagster_pipeline1_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)

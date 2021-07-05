from setuptools import find_packages, setup

setup(
    name="src",
    version="0.0.1",
    author="Elliott Lawrence",
    author_email="author@example.com",
    description="This project looks to investigate if there is a connection between clusters of ocean temperature in the southern hemisphere and the properties of the Southern Annular Mode (SAM)",
    url="url-to-github-page",
    packages=find_packages(),
    test_suite="src.tests.test_all.suite",
)

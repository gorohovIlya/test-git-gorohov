from setuptools import setup, find_packages

setup(
    name = "income_tax",
    version = "0.0.0",
    long_description = "Calculator of income tax in Russia",
    long_description_content_type = "text/markdown",
    author = "Ilya Gorokhov",
    author_email = "ilya.gorohov.404@gmail.com",
    license = "MIT",
    url = "https://github.com/gorohovIlya/test-git-gorohov/tree/feature/testing-tdd#",
    package_dir = {"": "src"},
    packages = find_packages(where="src"),
    python_requires=">=3",
)

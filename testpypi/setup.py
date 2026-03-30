from setuptools import setup, find_packages

setup(
    name="Russian_taxes_calculator",
    version="1.0",
    long_description_content_type = "text/markdown",
    long_description="Provides a function to calculate different tax types in Russia: Income tax, VAT, property tax, profit tax.",
    license='MIT',
    author="Ilya Gorokhov and Sergey Pleskunov",
    author_email="ilya.gorohov.404@gmail.com",
    url="https://github.com/gorohovIlya/test-git-gorohov/tree/homework-TestPyPi2",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)

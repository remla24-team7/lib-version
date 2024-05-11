from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="remla24-team7-lib-version",
    version='0.0.1',
    url='https://github.com/remla24-team7/lib-version',
    author='Kevin Tran',
    description='A version-aware library that can can be asked for the version of the library.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=['utility', 'versioning'],
    extras_require = {
        "dev": ["twine>=4.0.2"]
    }
)
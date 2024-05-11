from setuptools import find_packages, setup
from os.path import dirname, isdir, join
import os
import re
import subprocess


with open("README.md", "r") as f:
    long_description = f.read()


"""
Code used from: https://gist.github.com/pwithnall/7bc5f320b3bdf418265a
"""

version_re = re.compile('^Version: (.+)$', re.M)

def get_version():
    d = dirname(__file__)

    if isdir(join(d, '.git')):
        # Get the version using "git describe".
        cmd = 'git describe --tags --match v[0-9]*'.split()
        try:
            version = subprocess.check_output(cmd).decode().strip()
        except subprocess.CalledProcessError:
            print('Unable to get version number from git tags')
            exit(1)

        # PEP 386 compatibility
        if '-' in version:
            version = '.post'.join(version.split('-')[:2])

        # Don't declare a version "dirty" merely because a time stamp has
        # changed. If it is dirty, append a ".dev1" suffix to indicate a
        # development revision after the release.
        with open(os.devnull, 'w') as fd_devnull:
            subprocess.call(['git', 'status'],
                            stdout=fd_devnull, stderr=fd_devnull)

        cmd = 'git diff-index --name-only HEAD'.split()
        try:
            dirty = subprocess.check_output(cmd).decode().strip()
        except subprocess.CalledProcessError:
            print('Unable to get git index status')
            exit(1)

        if dirty != '':
            version += '.dev1'

    else:
        # Extract the version from the PKG-INFO file.
        with open(join(d, 'PKG-INFO')) as f:
            version = version_re.search(f.read()).group(1)

    return version

setup(
    name="remla24-team7-lib-version",
    version=get_version(),
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
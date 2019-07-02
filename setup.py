# Part of the awpa package: https://github.com/pyga/awpa
# See LICENSE for copyright.

from setuptools import setup, find_packages

import versioneer


with open('README.rst', 'r') as infile:
    long_description = infile.read()


setup(
    name='awpa',
    description='A Working Python AST',
    long_description=long_description,
    author='Aaron Gallagher',
    author_email='_@habnab.it',
    url='https://github.com/pyga/awpa',
    license='PSF/MIT',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    packages=find_packages(),
    include_package_data=True,
)

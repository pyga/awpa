# Part of the awpa package: https://github.com/habnabit/awpa
# See LICENSE for copyright.

from setuptools import setup, find_packages

import versioneer


setup(
    name='awpa',
    author='Aaron Gallagher',
    author_email='_@habnab.it',
    url='https://github.com/habnabit/awpa',
    license='PSF/MIT',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    packages=find_packages(),
    include_package_data=True,
)

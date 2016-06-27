# Copyright (c) Aaron Gallagher <_@habnab.it>
# See LICENSE for details.

from setuptools import setup, find_packages

import versioneer


setup(
    name='awpa',
    license='Apache 2',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    packages=find_packages(),
    include_package_data=True,
)

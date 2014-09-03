#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014 Raphaël Barrois
# This software is distributed under the GPLv3+ license.


import codecs
import os
import re
import sys

from setuptools import setup

root_dir = os.path.abspath(os.path.dirname(__file__))


def get_version(package_name):
    version_re = re.compile(r"^__version__ = [\"']([\w_.-]+)[\"']$")
    init_path = os.path.join(root_dir, package_name)
    with codecs.open(init_path, 'r', 'utf-8') as f:
        for line in f:
            match = version_re.match(line[:-1])
            if match:
                return match.groups()[0]
    return '0.1.0'


PACKAGE = 'bicti'


setup(
    name=PACKAGE,
    version=get_version(PACKAGE),
    description="Bicti, efficient startup script for within docker containers",
    long_description=''.join(codecs.open('README.rst', 'r', 'utf-8').readlines()),
    author="Raphaël barrois",
    author_email="raphael.barrois+%s@polytechnique.org" % PACKAGE,
    license="GPLv3+",
    keywords=['docker', 'container', 'init', 'startup'],
    url="https://github.com/rbarrois/%s/" % PACKAGE,
    download_url="https://pypi.python.org/pypi/%s/" % PACKAGE,
    platforms=["OS Independent"],
    scripts=[
        PACKAGE,
    ],
    setup_requires=[
        'setuptools>=0.8',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Build Tools",
        "Topic :: System :: Boot :: Init",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Software Distribution",
        "Topic :: System :: Systems Administration",
    ],
    zip_safe=False,
)


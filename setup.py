__author__ = 'vikesh'

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='fabulous',
    version='0.0.1',
    description='Answer to all your queries right inside Slack!',
    author='Eulercoder',
    author_email='hi@eulercoder.me',
    url='https://github.com/Eulercoder/fabulous',
    license='BSD-3-Clause',
    classifiers=(),
)
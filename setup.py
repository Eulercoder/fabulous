__author__ = 'vikesh'

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

PYTHON3 = sys.version_info[0] > 2

required = []
if not PYTHON3:
    required += ['importlib>=1.0.4']

packages = ['fabulous', 'fabulous.services']

try:
    longdesc = open('README.md').read()
except:
    longdesc = ''

setup(
    name='fabulous',
    version='0.0.1',
    description='Answer to all your queries right inside Slack!',
    author='Eulercoder',
    author_email='hi@eulercoder.me',
    url='https://github.com/Eulercoder/fabulous',
    packages=packages,
    scripts= ['bin/fabulous'],
    package_data={'': ['LICENSE',], '': ['fabulous/services/*.py']},
    include_package_data=True,
    install_requires=required,
    license='BSD-3-Clause',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)

#!/usr/bin/env python

import os
import sys
from setuptools import setup

# load __version__ without importing anything
version_file = os.path.join(
    os.path.dirname(__file__),
    'lobby/version.py')
with open(version_file, 'r') as f:
    # use eval to get a clean string of version from file
    __version__ = eval(f.read().strip().split('=')[-1])

# load README.md as long_description
long_description = ''
if os.path.exists('README.md'):
    with open('README.md', 'r') as f:
        long_description = f.read()

setup(name='lobby',
      version=__version__,
      description='Simulate market and limit orders.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Michael Dawson-Haggerty',
      author_email='mikedh@kerfed.com',
      license='MIT',
      url='https://github.com/mikedh/lobby',
      keywords='trading simulation market limit order',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Natural Language :: English',
          'Topic :: Scientific/Engineering'],
      packages=['lobby'],
      install_requires=[]
      )

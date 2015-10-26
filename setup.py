#!/usr/bin/env python

from distutils.core import setup

import os


VERSION_PREFIX = '# Version: '


def get_confusables_version():
  with open(os.path.join(os.path.dirname(__file__),
                         'confusables/confusables.txt')) as f:
    for line in f:
      line = line.strip()
      if line.startswith(VERSION_PREFIX):
        return line[len(VERSION_PREFIX):]

setup(name='confusables',
      version='0.1.' + get_confusables_version().replace('.', ''),
      url='https://github.com/rfw/confusables',
      description='Unicode TR39 confusable detection.',
      author='Tony Young',
      author_email='tony@rfw.name',
      packages=['confusables'],
      package_data={'confusables': ['confusables.txt']})

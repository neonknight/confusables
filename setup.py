#!/usr/bin/env python3

from distutils.core import setup, Extension
from distutils.command.build_ext import build_ext
from Cython.Build import cythonize

import os
import requests
import subprocess


VERSION_PREFIX = '# Version: '

cf = requests.get(
    'http://www.unicode.org/Public/security/latest/confusables.txt',
    stream=True).raw

for line in cf:
  line = line.decode('utf-8').lstrip('\ufeff').strip()
  if line.startswith(VERSION_PREFIX):
    unicode_version = line[len(VERSION_PREFIX):]
    break

class my_build_ext(build_ext):
  def run(self):
    import gen_confusables_table
    with open('src/confusables-table.gen.h', 'w') as f:
      gen_confusables_table.gen_confusables_table(f, cf)
    build_ext.run(self)


setup(name='confusables',
      version='0.2.' + unicode_version.replace('.', ''),
      url='https://github.com/rfw/confusables',
      description='Unicode TR39 confusable detection.',
      author='Tony Young',
      author_email='tony@rfw.name',
      cmdclass=dict(build_ext=my_build_ext),
      py_modules=['confusables'],
      ext_modules=cythonize([Extension('_confusables',
                                       sources=['src/_confusables.pyx'])]))

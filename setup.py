#!/usr/bin/env python3
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

import gen_confusables_table

VERSION_PREFIX = '# Version: '

cf = gen_confusables_table.get_confusables_file()


# this delays import of Cython to a moment when it is installed
class lazy_cythonize(list):
    def __init__(self, callback):
        self._list, self.callback = None, callback

    def c_list(self):
        if self._list is None: self._list = self.callback()
        return self._list

    def __iter__(self):
        for e in self.c_list(): yield e

    def __getitem__(self, ii): return self.c_list()[ii]

    def __len__(self): return len(self.c_list())


def extensions():
    from Cython.Build import cythonize
    ext = Extension('_confusables', sources=['src/_confusables.pyx'])
    return cythonize(ext)


for line in cf:
  line = line.decode('utf-8').lstrip('\ufeff').strip()
  if line.startswith(VERSION_PREFIX):
    unicode_version = line[len(VERSION_PREFIX):]
    break


class my_build_ext(build_ext):
  def run(self):
    with open('src/confusables-table.gen.h', 'w') as f:
      gen_confusables_table.gen_confusables_table(f, cf)
    build_ext.run(self)

requires = ['cython']


setup(
    name='confusables',
    version='0.5.' + unicode_version.replace('.', ''),
    url='https://github.com/rfw/confusables',
    description='Unicode TR39 confusable detection.',
    author='Tony Young',
    author_email='tony@rfw.name',
    cmdclass=dict(build_ext=my_build_ext),
    py_modules=['confusables'],
    setup_requires=requires,
    install_requires=requires,
    ext_modules=lazy_cythonize(extensions)
)

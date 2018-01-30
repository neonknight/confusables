#!/usr/bin/env python
from __future__ import unicode_literals

import os
try:
  #python2
  from urllib import urlretrieve
  char = unichr
except ImportError:
  #python3
  from urllib.request import urlretrieve
  char = chr


def get_confusables_file():
  if not os.path.exists('src/confusables.txt'):
    print('retrieving latest confusables.txt')
    req = urlretrieve(
        'http://www.unicode.org/Public/security/latest/confusables.txt',
        'src/confusables.txt')
  return open('src/confusables.txt', 'rb')


def build_confusables_table(cf):
  confusables = {}

  for line in cf:
    line = line.decode('utf-8').lstrip('\ufeff')

    try:
      i = line.index('#')
    except ValueError:
      pass
    else:
      line = line[:i]

    line = line.strip()
    if not line:
      continue

    src, tgt, _ = line.split(' ;\t')

    src = int(src, 16)
    tgt = ''.join(char(int(t, 16)) for t in tgt.split(' '))

    confusables[src] = tgt

  return confusables


def gen_confusables_table(f, cf):
  confusables = build_confusables_table(cf)

  for k, v in confusables.items():
    f.write('static char const confusable_{:08x}[] = "{}";\n'
        .format(k, ''.join('\\x{:02x}'.format(t) for t in v.encode('utf-8'))))

  f.write('\nstatic char const* CONFUSABLES[] = {\n')

  for i in range(max(confusables.keys()) + 1):
    f.write('    ')
    f.write('confusable_{:08x}'.format(i) if i in confusables else '0')
    f.write(',\n')

  f.write('};\n')

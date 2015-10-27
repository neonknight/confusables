#!/usr/bin/env python3

import os


def gen_confusables_table(f, cf):
  confusables = {}

  max_tgt_size = 0

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
    tgt = tuple(int(t, 16) for t in tgt.split(' '))

    confusables[src] = tgt
    max_tgt_size = max(len(tgt), max_tgt_size)

  f.write('#include <stdint.h>\n\n')

  for k, v in confusables.items():
    f.write("static uint32_t const confusable_{:08x}[] = {{{}, 0}};\n"
        .format(k, ', '.join('0x{:08x}'.format(t) for t in v)))

  f.write('\nstatic uint32_t const* CONFUSABLES[] = {\n')

  for i in range(max(confusables.keys()) + 1):
    f.write('    ')
    f.write('confusable_{:08x}'.format(i) if i in confusables else '0')
    f.write(',\n')

  f.write('};\n')

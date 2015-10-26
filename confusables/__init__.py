import os
import unicodedata


def _make_replacements():
  replacements = {}

  with open(os.path.join(os.path.dirname(__file__), 'confusables.txt')) as f:
    for line in f:
      line = line.lstrip('\ufeff')

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

      src = chr(int(src, 16))
      tgt = ''.join(chr(o) for o in (int(c, 16) for c in tgt.split(' ')))

      replacements[src] = tgt

  return replacements

_REPLACEMENTS = _make_replacements()


def skeleton(s):
  """The skeleton function, as described by Unicode TR39.

  To see whether two strings X and Y are confusable (abbreviated as X ≅ Y), an
  implementation uses a transform of X called a skeleton(X) defined by:

  1. Converting X to NFD format, as described in UAX15.

  2. Successively mapping each source character in X to the target string
     according to the specified data.

  3. Reapplying NFD.

  Read more: http://unicode.org/reports/tr39/#Confusable_Detection
  """
  return unicodedata.normalize('NFD',
    ''.join(_REPLACEMENTS.get(c, c) for c in unicodedata.normalize('NFD', s)))

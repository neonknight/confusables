import _confusables

import unicodedata


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
    ''.join(_confusables.lookup_confusable(c) or c
        for c in unicodedata.normalize('NFD', s)))

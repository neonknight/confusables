from libc.stdint cimport uint32_t

cdef extern from "confusables.h":
  const uint32_t* const lookup_confusable(uint32_t confusable)

def _lookup_confusable(c):
  confusable = lookup_confusable(ord(c))
  ret = []

  i = 0
  while confusable[i] != 0:
    ret.append(chr(confusable[i]))
    i += 1

  return u''.join(ret)

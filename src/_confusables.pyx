from libc.stdint cimport uint32_t

cdef extern from "confusables-table.gen.h":
  const uint32_t* CONFUSABLES[]

def lookup_confusable(c):
  confusable = CONFUSABLES[ord(c)]

  if not confusable:
    return None

  ret = []

  i = 0
  while confusable[i] != 0:
    ret.append(chr(confusable[i]))
    i += 1

  return u''.join(ret)

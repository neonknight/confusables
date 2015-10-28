from libc.stdint cimport uint32_t

cdef extern from "confusables-table.gen.h":
  const uint32_t* CONFUSABLES[]

def lookup_confusable(c):
  confusable = <const uint32_t*> CONFUSABLES[ord(c)]

  if not confusable:
    return None

  chars = []

  i = 0
  while confusable[i] != 0:
    chars.append(chr(confusable[i]))
    i += 1

  return u''.join(chars)

cdef extern from "confusables-table.gen.h":
  const char* CONFUSABLES[]

def lookup_confusable(c):
  confusable = <const char*> CONFUSABLES[ord(c)]

  if not confusable:
    return None

  return confusable.decode('utf-8')

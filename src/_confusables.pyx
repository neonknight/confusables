ctypedef const char* confusables_ptr

cdef extern from 'confusables-table.gen.h':
  confusables_ptr CONFUSABLES[]

def lookup_confusable(c):
  o = ord(c)

  if o >= sizeof(CONFUSABLES) / sizeof(confusables_ptr):
    return None

  confusable = <confusables_ptr> CONFUSABLES[o]

  if not confusable:
    return None

  return confusable.decode('utf-8')

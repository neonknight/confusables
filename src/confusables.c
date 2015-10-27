#include "confusables.h"

#include "confusables-table.gen.h"

static int MAX_CONFUSABLE = sizeof(CONFUSABLES) / sizeof(CONFUSABLES[0]);
static uint32_t const EMPTY[] = {0};

uint32_t const* const lookup_confusable(uint32_t confusable) {
  if (confusable >= MAX_CONFUSABLE) {
    return EMPTY;
  }

  return CONFUSABLES[confusable];
}

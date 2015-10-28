import confusables
import gen_confusables_table
import unittest


class TestConfusables(unittest.TestCase):
  def test_confusable_zero(self):
    self.assertEqual('\0', confusables.skeleton('\0'))


def generate_methods():
  confusables_table = gen_confusables_table.build_confusables_table(
      gen_confusables_table.get_confusables_file())

  test_methods = {}

  for k, v in confusables_table.items():
    def test_method(self):
      self.assertEqual(v, confusables.skeleton(chr(k)))
    setattr(TestConfusables, "test_confusable_{:08x}".format(k), test_method)

  def test_confusable_out_of_bounds(self):
    max_confusable_plus_one = chr(max(confusables_table.keys()) + 1)
    self.assertEqual(max_confusable_plus_one,
                     confusables.skeleton(max_confusable_plus_one))

  setattr(TestConfusables, "test_confusable_out_of_bounds",
          test_confusable_out_of_bounds)

generate_methods()


if __name__ == '__main__':
  unittest.main()

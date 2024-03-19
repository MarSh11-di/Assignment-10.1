import unittest


def calculate_average(numbers):
   return sum(numbers) / len(numbers)


class TestCalculateAverage(unittest.TestCase):

   def test_calculate_average_whole(self):
      numbers = [1, 2, 3, 4, 5]
      expected_result = 3
      actual_resalt = calculate_average(numbers)
      self.assertEqual(actual_resalt, expected_result)

   def test_calculate_average_decimal(self):
      numbers = [1.2, 2.2, 3.3, 4.2, 5.2]
      expected_result = 3.22
      actual_resalt = calculate_average(numbers)
      self.assertAlmostEqual(actual_resalt, expected_result)

   def test_calculate_average_empty(self):
      with self.assertRaises(ZeroDivisionError):
         calculate_average([])

# To run the tests:
unittest.main(argv=[''], exit=False)
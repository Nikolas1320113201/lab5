import unittest
from lab2 import Calculator

class TestCalculator(unittest.TestCase):
  test = Calculator(2)
  
  def n_chlen_test(self):
    self.assertEqual(self.test.n_chlen(3), 7)

if __name__ == "__main__":
  import xmlrunner
  runner = xmlrunner.XMLTestRunner(output='test-reports')
  unittest.main(testRunner=runner)
  unittest.main()


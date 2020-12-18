import unittest
from lab2 import length


class TestProgression(unittest.TestCase):
    test = length(2)

    def test_add(self):
        self.assertEqual(self.test.__add__(3), 7)


if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    
    unittest.main()


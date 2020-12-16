import unittest
from lab2 import length


class TestProgression(unittest.TestCase):
    test = length(8.67)
    test2 = length(0.89)

    def test_add(self):
        self.assertEqual(self.test.__add__(0.67), 9.34)
        self.assertEqual(self.test.__add__(10), 18.67)
        self.assertTrue(self.test.__add__(1),isinstance(self.test.__add__(1),float))
        self.assertEqual(self.test2.__add__(1), 1.8900000000000001)
        self.assertEqual(self.test2.__add__(5), 5.89)

    def test_sub(self):
        self.assertRaises(TypeError,self.test.__sub__,'str')
        self.assertEqual(self.test.__sub__(0.67), 8)
        self.assertEqual(self.test2.__sub__(0.8), 0.08999999999999997)


    def test_mul(self):
        self.assertEqual(self.test.__mul__(3), 26.009999999999998)
        self.assertEqual(self.test2.__mul__(7),6.23)
        self.assertRaises(TypeError,self.test.__mul__,0.5)

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    
    unittest.main()

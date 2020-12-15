""" Tests for maths.py """
import unittest
import app as tested_app
import json

class FlaskAppTests(unittest.TestCase)


    
    def SetUp(self):
        self.app = tested_app.app.test_client()
    
    
    def test_get_hello_endpoint(self):
        r = self.app.get('/')
        self.assertEqual(r.status, '200 OK')
        self.assertEqual(r.data, b'Hello world from app!! It is Pipeline testing.')
        
if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    
unittest.main()
        




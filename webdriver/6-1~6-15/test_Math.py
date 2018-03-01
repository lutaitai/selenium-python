from calculator import *
import unittest

class TMath(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_add(self):
        j=Math(5,10)
        self.assertEqual(j.add(),15)
        # self.assertEqual(j.add(),12)

    def test_add_a2(self):
        j=Math(5,10)
        self.assertNotEqual(j.add,12)

    def test_assertTrue_a3(self):
        j=Math(5,10)
        self.assertTrue(j.add()>10)

    def test_assertIn_a4(self):
        self.assertIn("8888","hello,51zxw")

    def test_assertIs_a5(self):
        self.assertIs("51zxw","51zxw")

    def tearDown(self):
        print("Test end")

if __name__=='__main__':
    # case = unittest.defaultTestLoader.loadTestsFromTestCase(TMath.test_assertIn_a4)
    suite=unittest.TestSuite()
    suite.addTest(TMath("test_add_a2"))

    runer=unittest.TextTestRunner()
    runer.run(suite)
    # unittest.main()

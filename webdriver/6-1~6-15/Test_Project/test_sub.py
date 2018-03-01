from calculator import *
from StartEnd import *

class Test_sub(Setup_tearDown):
    def test_sub(self):
        i=Math(5,5)
        self.assertEqual(i.sub(),0)

    def test_sub1(self):
        i=Math(5,3)
        self.assertEqual(i.sub(),2)
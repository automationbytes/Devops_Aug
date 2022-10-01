import unittest

class AssertionTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(1+2,3)

    def test2(self):
        self.assertNotEqual(1+2,13)

    def test3(self):
        self.assertTrue(1+2 == 13,"The result is false")

    def test4(self):
        self.assertFalse(1+2 == 3)

    def test5(self):
        self.assertAlmostEqual(5.555555555,5.555555556,places=30)

    def test6(self):
       # self.assertIn("v","sachin")

        li = {2,3,4}
        li2 = {3,2,5}
        self.assertSetEqual(li,li2)
'''
test
setUp - prestep
teardown - post step

'''

import unittest

def setUpModule():
    print("Its setup Module")

def tearDownModule():
    print("Its tearDOwn Module")



class sampletest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Its setup class")

    def setUp(self):
        print("Its setup test")

    def test1(self):
        print("Test 1")

    def test2(self):
        print("Test 2")

    def tearDown(self):
        print("Its Teardown test")


    @classmethod
    def tearDownClass(cls):
        print("Its tearDown class")

    if __name__ == '__main__':
        unittest.main()
'''
unittest.skip(reason)- without any condition check
unittest.skipIf(condition,reason) - if the condition satisfy, then it will skip
unittest.skipUnless(condition,reason) - if the condition is false, it will skip
unittest.expectedFailure()-

'''

import unittest

class skip_Test(unittest.TestCase):

    def test1(self):
        print("Test 1")
    @unittest.skip("Just skip")
    def test2(self):
        print("Test 2")

    @unittest.skipIf(1 == 1, "Skip if the condition is true")
    def test3(self):
        print("Test 3")

    def test4(self):
        print("Test 4")

    @unittest.skipUnless(1 == 0,"Skip if it is false")
    def test5(self):
        print("Test 5")

    def test6(self):
        print("Test 6")
    @unittest.expectedFailure
    def test7(self):
        print("Test 7")

if __name__ == '__main__':
    unittest.main()
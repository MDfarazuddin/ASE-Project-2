# Make sure to send me your algorithms. Ill write the unittest or doctest(whicever is necessary).
# This is the base for unittest.

import unittest

#  Add your code here in a function or import it here

# This is a test ive written to show how it works
def add(a,b):
    return a+b

class SuryaTest(unittest.TestCase):
    def test(self):
        self.assertTrue(True)
    def test2(self):
        self.assertEqual(add(2,3),5)
    def test3(self):
        self.assertEqual(add(2,3),3)
    # Add a function here that starts with 'test' 
    # Make sure to use appropriate assertxxxx(funct(a,b,c,d,...),X)

if __name__ == "__main__":
    unittest.main()       

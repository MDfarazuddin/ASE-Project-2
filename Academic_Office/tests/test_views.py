from django.test import TestCase
from django.test import Client

class YourTestClassTrial(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("Tests Start here, Send your algorithms so i can add it here")
        pass

    def setUp(self):
        print("Code here runs before every test so you can write your names if you want.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_one_plus_one_equals_two(self):
        print("Basic understanding of how testing works you can add your function based on this example")
        self.assertEqual(1 + 1, 2)

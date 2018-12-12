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
    def test_one_plus_one_equals_two(self):
        print("Basic understanding of how testing works you can add your function based on this example")
        self.assertEqual(1 + 1, 2)
class testlogin(TestCase):
    # Testing if any url is available without logging in
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('Admin/add-student')
        self.assertEqual(response.status_code, 404)
    def test_view_url_exists_at_desired_location2(self):
        response = self.client.get('Admin/Admin/add-teacher/')
        self.assertEqual(response.status_code, 404)
    def test_view_url_exists_at_desired_location3(self):
        response = self.client.get('Admin/all/students/')
        self.assertEqual(response.status_code, 404)
    def test_view_url_exists_at_desired_location4(self):
        response = self.client.get('Admin/all/students/2017001108')
        self.assertEqual(response.status_code, 404)
    def test_view_url_exists_at_desired_location5(self):
        response = self.client.get('Admin/all/teachers/003')
        self.assertEqual(response.status_code, 404)
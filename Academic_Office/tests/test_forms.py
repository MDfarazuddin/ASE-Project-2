from django.test import TestCase
from Admin.forms import Register_student,Register_teacher
from Student.forms import Login_student
class Testinfforms(TestCase):
    def test_forms(self):
        data = {'S_name':'teststudnet','S_id':'9999','S_email':'test@test.com','password':'testpass','re_password':'testpass'}
        # Should fail because i haven't mentioned any courses
        form = Register_student(data=data)
        print("________________________\n")
        print(form.errors)
        print("_________________________\n")
        self.assertFalse(form.is_valid())

    def test_forms2stu(self):
        data = {'username':'2017001049','password':'password123'}
        form2 = Login_student(data=data)
        self.assertTrue(form2.is_valid())

    def test_forms2tea(self):
        data = {'T_id':'999','T_name':'password','T_email':'surya@srikanth.com','T_course_id':'philosophy','slug':'999','password':'hellopass','re_password':'hellopass'}
        form3 = Register_teacher(data=data)
        # Failed because course id that is not available is given
        print("______________Error 2______________\n")
        print(form3.errors)
        print("______________________________")
        self.assertFalse(form3.is_valid())
from django.test import TestCase
from Teacher.models import Teachers,Announcements
from Student.models import Courses,Assignment
from Admin.models import Admins


# Students and teachers models test
class test_teacher(TestCase):
    @classmethod
    def setUpmodelTest(cls):
        print("One should FAIL")

    def Create_model1(self):
        try:
            Teach = Courses.objects.create(C_name='testc')
            # Should fail because i have given wrong foreign key connection
            return Teachers.objects.create(T_id='123456789', T_name='testteach',T_course_id=Teach.C_name, slug = '123',T_email="ttest@test.com", T_password='123456789' )
        except:
            return False

    def Create_model_announce(self):
        try:
            name = Teachers.objects.create(T_id='123',T_course_id_id='123',T_password='123',T_email='test@test.com',T_name='testteacher')
            # Should fail because slug
            return Announcements.objects.create(T_id = name.T_id,T_date='yesterday',T_comment='hello test fail')
        except:
            return False
    def Create_model_assig(self):
        return Assignment.objects.create(A_id='test123',A_marks="100",A_max_marks='1000',A_weightage='10')

    def test_models(self):
        t = self.Create_model1()
        self.assertFalse(t)
    def test_assignmentmodel(self):
        a = self.Create_model_assig()
        self.assertTrue(isinstance(a,Assignment))
    def test_announcemodel(self):
        ann = self.Create_model_announce()
        self.assertFalse(ann)

# Admin Models test
class test_admin(TestCase):
    def Create_model2(self):
        return Admins.objects.create(A_id='12345dellsurya',A_name='SuryaSrikanth', A_password='Suryatest123')
    def test_model2(self):
        A = self.Create_model2()
        self.assertTrue(isinstance(A,Admins))
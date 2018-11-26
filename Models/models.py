
from django.db import models

# Create your models here.
class Profile(models.Model):
    SID=models.CharField(max_length=10,primary_key=True)
    Student_name=models.CharField(max_length=250)
    grade = models.CharField(max_length=3)

class Teacher(models.Model):
    TID=models.CharField(max_length=10,primary_key=True)
    Teacher_name=models.CharField(max_length=250)

class Courses(models.Model):
    CID = models.CharField(max_length=3,primary_key=True)
    C_name=models.CharField(max_length=100)
    TID=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    Credits=models.CharField(max_length=2)

class Attendance(models.Model):
    CID = models.ForeignKey(Courses,on_delete=models.CASCADE)
    SID = models.ForeignKey(Profile, on_delete=models.CASCADE)
    dates = models.DateField(null=True)
    Y_N=models.CharField(max_length=1)
    Topic_name=models.CharField(max_length=100)

class Marks(models.Model):
    CID = models.ForeignKey(Courses, on_delete=models.CASCADE)
    SID = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Ass_ID = models.CharField(max_length=50)
    marks_obtained = models.CharField(max_length=3)

class Weightage(models.Model):
    CID = models.ForeignKey(Courses, on_delete=models.CASCADE)
    Ass_ID = models.ForeignKey(Marks, on_delete=models.CASCADE)
    weightage = models.CharField(max_length=3)
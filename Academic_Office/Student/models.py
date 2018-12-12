from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.


class Courses(models.Model):
    C_id = models.CharField(max_length=3 ,primary_key=True)
    C_name = models.CharField(max_length=15)
    C_credits=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    # C_books = models.ManyToManyField(Book,blank=True)
    def __str__(self):
        return self.C_name



class Book(models.Model): 
    B_cid = models.ForeignKey(Courses,on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

class Students(models.Model):
    S_id=models.CharField(max_length=10,primary_key=True)
    S_name=models.CharField(max_length=250)
    slug = models.SlugField()
    S_email = models.EmailField(blank=True,default="farazuddin.m17@iiits.in")
    S_password = models.CharField(max_length=50)
    S_courses = models.ManyToManyField(Courses)
    S_cgpa = models.FloatField(default=0)
    def __str__(self):
    	return self.S_name


class Assignment(models.Model):
    A_id = models.CharField(max_length=10, primary_key=True)
    A_max_marks = models.IntegerField()
    A_course = models.ForeignKey(Courses,on_delete=models.CASCADE,default='001')

    def __str__(self):
        return self.A_id

class GradingPolicy(models.Model):
    G_assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE)
    G_weightage = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],default=0)

    def __str__(self):
        return self.G_assignment.A_id

class AssignMarks(models.Model):
    A_sid = models.ForeignKey(Students,on_delete=models.CASCADE)
    A_id = models.ForeignKey(Assignment,on_delete=models.CASCADE)
    A_marks = models.IntegerField(default=0)

    def __str__(self):
        return str(self.A_sid) + ' ' + str(self.A_id)

class FinalGradePolicy(models.Model):
    F_course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    F_s = models.IntegerField(default=0)
    F_a = models.IntegerField(default=0)
    F_b = models.IntegerField(default=0)
    F_c = models.IntegerField(default=0)
    F_d = models.IntegerField(default=0)

    def __str__(self):
        return self.F_course.C_name

class FinalMarks(models.Model):
    F_sid = models.ForeignKey(Students,on_delete=models.CASCADE)
    F_course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    F_marks = models.FloatField(default=0)
    F_grade = models.CharField(max_length=1,default='F')

    def __str__(self):
        return self.F_sid.S_name+" "+self.F_course.C_name
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Courses(models.Model):
    C_id = models.CharField(max_length=3 ,primary_key=True)
    C_name = models.CharField(max_length=15)
    C_credits=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    def __str__(self):
        return self.C_name

class Students(models.Model):
    S_id=models.CharField(max_length=10,primary_key=True)
    S_name=models.CharField(max_length=250)
    slug = models.SlugField()
    S_email = models.EmailField(blank=True,default="farazuddin.m17@iiits.in")
    S_password = models.CharField(max_length=50)
    S_courses = models.ManyToManyField(Courses)
    def __str__(self):
    	return self.S_name

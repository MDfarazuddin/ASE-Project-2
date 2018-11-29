from django.db import models
from Student.models import Courses
# Create your models here.
class Teachers(models.Model):
	T_id = models.CharField(max_length = 15)
	T_name = models.CharField(max_length = 20)
	T_course_id = models.ForeignKey(Courses,on_delete=None)
	slug = models.SlugField()
	T_email = models.EmailField(default="farazuddin.m17@iiits.in",blank=True)
	T_password=models.CharField(max_length=50)
	def __str__(self):
		return self.T_name

from django.db import models
from Student.models import *
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

class Announcements(models.Model):
	A_tid = models.ForeignKey(Teachers,on_delete=models.CASCADE)
	A_comment = models.CharField(max_length=1000)
	A_date = models.CharField(max_length=50)


class finalAttendance(models.Model):
	student = models.ForeignKey(Students, on_delete=models.CASCADE)
	course = models.ForeignKey(Courses, on_delete=models.CASCADE)
	present = models.IntegerField(default=0)
	total = models.IntegerField(default=0)

	def __str__(self):
		return str(self.student) + " " + str(self.course)
class DatewiseAttendance(models.Model):
	student = models.ForeignKey(Students, on_delete=models.CASCADE)
	course = models.ForeignKey(Courses, on_delete=models.CASCADE)
	date = models.DateField()
	present = models.IntegerField(default=1,validators=[MinValueValidator(0), MaxValueValidator(1)])
	__lastvalue = 1
	def save(self, *args, **kwargs):
		self.finallink, created = finalAttendance.objects.get_or_create(student= self.student, course=self.course)
		
		if self.id:
			if self.__lastvalue != self.present:
				self.__lastvalue = self.present
				if self.present == 0:
					self.finallink.present -= 1
				else:
					self.finallink.present += 1
		else:
			self.__lastvalue = self.present
			self.finallink.present += self.present
			self.finallink.total += 1
			self.finallink.save()
		
			
		super(DatewiseAttendance, self).save(*args, **kwargs)
		
	def delete(self, *args, **kwargs):
		self.finallink.total -= 1
		self.finallink.present -= self.present
		self.finallink.save()
		super(DatewiseAttendance, self).delete(*args, **kwargs)
		
	def __str__(self):
		return str(self.student) + " " + str(self.date)

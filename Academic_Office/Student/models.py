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
    def __str__(self):
    	return self.S_name

import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Name(models.Model):
    name_text = models.CharField(max_length=200)

    def __str__(self):
        return self.name_text

class Comment(models.Model):
    name_text = models.ForeignKey(Name, on_delete=models.CASCADE)
    comm_text = models.CharField(max_length=500)
   # likes = models.IntegerField(default=0)    
    def __str__(self):
        return self.comm_text
    

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Students)
admin.site.register(Courses)
admin.site.register(Book)
admin.site.register(Assignment)
admin.site.register(AssignMarks)
admin.site.register(GradingPolicy)
admin.site.register(FinalGradePolicy)
admin.site.register(FinalMarks)
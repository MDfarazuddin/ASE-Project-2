from django.shortcuts import render
from django.http import HttpResponse
from .models import Students
# Create your views here.
def Student_profile(request,slug):
	a_student = Students.objects.get(slug=slug)
	return render(request,'Student/Student_View.html',{"a_student":a_student})
	
def Student_courses(request,slug):
	a_student = Students.objects.get(slug=slug)
	return render(request,'Student/Student_View_Courses.html',{"a_student":a_student})
def Student_grade_sheet(request):
	return render(request,'Student/Student_View_Grade_Sheet.html')

def Student_course_page(request):
	return render(request,'Student/Student_View_Courses_details.html')
from django.shortcuts import render
from django.http import HttpResponse
from .models import Students,Courses,Book
# Create your views here.
def Student_profile(request,slug):
	a_student = Students.objects.get(slug=slug)
	return render(request,'Student/Student_View.html',{"a_student":a_student})
	
def Student_courses(request,slug):
	a_student = Students.objects.get(slug=slug)
	return render(request,'Student/Student_View_Courses.html',{"a_student":a_student})
def Student_grade_sheet(request):
	return render(request,'Student/Student_View_Grade_Sheet.html')

def Student_course_page(request,slug):
	a_course  = Courses.objects.get(C_id =slug)
	return render(request,'Student/Student_View_Courses_details.html',{'a_course':a_course})

def Student_assignment_list(request,slug):
	course = Courses.objects.get(C_id = slug)
	books = Book.objects.filter(B_cid = slug)
	return render(request,'Student/book_list.html',{'books':books,'course':course})
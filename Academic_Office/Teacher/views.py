from django.shortcuts import render

from django.http import HttpResponse

from . models import Teachers
from Student.models import Students,Courses

def Teacher_Profile(request,slug):
	a_teacher = Teachers.objects.get(slug=slug)
	return render(request,'Teacher/Teacher_View.html',{"a_teacher":a_teacher})

def Show_students(request,slug):
	a_teacher = Teachers.objects.get(slug=slug)
	course = a_teacher.T_course_id.C_id
	a = Students.objects.all()
	students_name = []
	students_id = []
	for x in a:
		if x.S_courses.filter(C_id = course):
			students_name.append(x.S_name)
			students_id.append(x.S_id)
	dict = {'name':students_name,'id':students_id}
	return render(request,'Teacher/Teacher_students_enrolled.html',dict)

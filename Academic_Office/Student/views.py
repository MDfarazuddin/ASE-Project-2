from django.shortcuts import render
from django.http import HttpResponse
from .models import Students
# Create your views here.
def Student_profile(request,slug):
	try:
		request.session['S_id']
		a_student = Students.objects.get(slug=slug)
		return render(request,'Student/Student_View.html',{"a_student":a_student})
	except:
		pass
	try:
		request.session['A_id']
		a_student = Students.objects.get(slug=slug)
		return render(request,'Student/Student_View.html',{"a_student":a_student})
	except:
		return HttpResponse('not logged in')

def Student_courses(request,slug):
	a_student = Students.objects.get(slug=slug)
	return render(request,'Student/Student_View_Courses.html',{"a_student":a_student})

def Student_grade_sheet(request):
	return render(request,'Student/Student_View_Grade_Sheet.html')

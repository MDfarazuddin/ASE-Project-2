from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from Teacher.models import *
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

def Student_assignment_list_1(request,slug):
	course = Courses.objects.get(C_id=slug)
	assignments = Assignment.objects.filter(A_course = course)
	return render(request,'Student/Student_View_assignments.html',{'assignments':assignments})



def Student_view_scores(request,slug):
	assignment_id = Assignment.objects.get(A_id=slug)
	x = AssignMarks.objects.filter(A_id=assignment_id)
	student_id = []
	student_name =[]
	marks = []
	for m in x:
		student = m.A_sid
		student_id.append(student.S_id)
		student_name.append(student)
		marks.append(m.A_marks)
	s_info = zip(student_id,student_name,marks)
	return render(request, 'Student/Student_View_marks.html',{'s_info':s_info,'a_id':assignment_id,'a_max':assignment_id.A_max_marks})


def Student_grade_sheet(request,slug):
	student  = Students.objects.get(S_id=slug)
	courses = student.S_courses.all()

	for m in courses:
		sum = 0
		student_grade = 'F'
		assignments = Assignment.objects.filter(A_course=m)
		for n in assignments:
			marks = AssignMarks.objects.get(A_sid=student, A_id=n)
			marks = marks.A_marks
			weightage = GradingPolicy.objects.get(G_assignment=n)
			weightage =int( weightage.G_weightage)
			max_marks = int(n.A_max_marks)
			if max_marks !=0:
				n_marks = marks/max_marks * weightage
			else:
				n_marks = 0
			sum = sum + n_marks
		grade = FinalGradePolicy.objects.get(F_course=m)
		if grade.F_s:
			if sum >= grade.F_s:
				student_grade = 'S'
			elif sum >= grade.F_a:
				student_grade = 'A'
			elif sum>=grade.F_b:
				student_grade = 'B'
			elif sum>=grade.F_c:
				student_grade = 'C'
			elif sum>= grade.F_d:
				student_grade = 'D'
			else:
				student_grade = 'F'
		obj = FinalMarks.objects.get(F_sid=student,F_course=m)
		obj.F_marks = sum
		obj.F_grade = student_grade
		obj.save()
	sum_credits = 0
	total = 0
	for x in courses:
		grade = FinalMarks.objects.get(F_sid=student, F_course=x)
		grade = grade.F_grade
		credit = Courses.objects.get(C_name=x)
		credit = credit.C_credits
		sum_credits += credit
		if grade == 'S':
			total += 10 * credit
		elif grade == 'A':
			total += 9 * credit
		elif grade == 'B':
			total += 8 * credit
		elif grade == 'C':
			total += 7*credit
		elif grade == 'D':
			total += 6 * credit
		else:
			total += 0
	x  = total/sum_credits
	rounded_cgpa  =("%.2f" % x)
	rounded_cgpa  = rounded_cgpa
	student.S_cgpa = rounded_cgpa
	student.save()

	grades = FinalMarks.objects.filter(F_sid = student)
	return render(request,'Student/Student_View_Grade_Sheet.html',{'grades':grades,'name':grades[0].F_sid,'cgpa':student.S_cgpa})

def view_announcements(request):
	all_comments= Announcements.objects.all()
	all_comments = all_comments[::-1]
	return render(request,'Student/student_announcements.html',{'ab':all_comments})	

def view_attendance(request,slug):
	student = Students.objects.get(S_id = slug)
	attendance=finalAttendance.objects.filter(student=student)
	name = student.S_name
	return render(request,'Student/Student_attendance.html',{'attendance':attendance,'name':name})
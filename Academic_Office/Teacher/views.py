from datetime import datetime
from django.shortcuts import render,redirect

from django.http import HttpResponse

from . models import *
from Student.models import *
from .forms import BookForm, AddAssignment


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



def Course_contents(request,slug):
	course= Courses.objects.get(C_id=slug)
	return render(request,'Teacher/Teacher_course_contents.html',{'courses':course})


def book_list(request,slug):
    books = Book.objects.filter(B_cid=slug)
    print("\n\n\n\n",Book.objects.filter(B_cid=slug))
    return render(request, 'Teacher/book_list.html', {
        'books': books
    })


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'Teacher/confirmed.html')
    else:
        form = BookForm()
    return render(request, 'Teacher/upload_book.html', {
        'form': form
    })


def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return render(request,'Teacher/confirmed.html')



def populate_marks( assignment):
	course = assignment.A_course
	student = Students.objects.all()
	for x in student:
		if x.S_courses.filter(C_id=course.C_id):
			obj = AssignMarks.objects.create(A_sid=x,A_id=assignment)
			obj.save()



def add_assignment(request):
	form = AddAssignment()
	if request.method == 'POST':
		form = AddAssignment(request.POST)
		if form.is_valid():
			instance = form.save()
			obj = GradingPolicy.objects.create(G_assignment=instance)
			obj.save()
			populate_marks(instance)
			return render(request,'Teacher/confirmed.html')
		else:
			return render(request, 'Teacher/Teacher_add_assignment.html', {'form':form})
	else:
		return render(request, 'Teacher/Teacher_add_assignment.html', {'form': form})


def set_grading_policy(request,slug):
	course = Courses.objects.get(C_id=slug)
	assignments = Assignment.objects.filter(A_course=course)
	list = []
	weightage = []
	for m in assignments:
		list.append(m.A_id)
		w1 = GradingPolicy.objects.get(G_assignment=m)
		weightage.append(w1.G_weightage)
	a = zip(list,weightage)
	message = ''
	if request.method == 'POST':
		sum = 0
		for m in list:
			w = Assignment.objects.get(A_id=m)
			w1= GradingPolicy.objects.get(G_assignment=w)
			print(request.POST)
			w1.G_weightage = int(request.POST[m])
			sum+= int(request.POST[m])
			w1.save()
		if sum <= 100:
			return render(request,'Teacher/confirmed.html')
		else:
			message = "Sum can't be more than 100"
			return render(request, 'Teacher/Teacher_add_weightage.html',{'a':a,'message':message})
	else:
		#return render(request, 'Teacher/Teacher_add_weightage.html',{'assignment':assignments, 'weightage':weightage})
		return render(request, 'Teacher/Teacher_add_weightage.html',{'a':a,'message':message})

def add_marks(request,slug):
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
	if request.method == "POST":
		for m in student_name:
			obj = AssignMarks.objects.get(A_sid=m, A_id=assignment_id)
			obj.A_marks = int(request.POST[m.S_id])
			obj.save()

		return render(request,'Teacher/confirmed.html')
		# return render(request, 'Teacher/Teacher_add_marks.html',{'s_info': s_info, 'a_id': assignment_id, 'a_max': assignment_id.A_max_marks})

	else:
		return render(request, 'Teacher/Teacher_add_marks.html',{'s_info':s_info,'a_id':assignment_id,'a_max':assignment_id.A_max_marks})


def Show_assignments(request,slug):
	course = Courses.objects.get(C_id=slug)
	assignments = Assignment.objects.filter(A_course = course)
	return render(request,'Teacher/Teacher_assignment_list.html',{'assignments':assignments})

def assignments(request,slug): 
	a_teacher = Teachers.objects.get(slug=slug)
	course = a_teacher.T_course_id.C_id
	course = Courses.objects.get(C_id = course)
	return render(request,'Teacher/Teacher_Set_Grading_Policy.html',{'course':course})

def check(x):
	if x.F_s > x.F_a and x.F_a > x.F_b and x.F_b > x.F_c and x.F_c > x.F_d:
		return True
	else:
		return False
def final_grade_policy(request,slug):
	course = Courses.objects.get(C_id=slug)
	grade_policy = FinalGradePolicy.objects.get(F_course = course)
	message = ""
	if request.method == 'POST':
		grade_policy.F_s = request.POST['S']
		grade_policy.F_a = request.POST['A']
		grade_policy.F_b = request.POST['B']
		grade_policy.F_c = request.POST['C']
		grade_policy.F_d = request.POST['D']
		if check(grade_policy):
			grade_policy.save()
			return render(request, 'Teacher/Teacher_set_final_grade_policy.html', {'context': grade_policy,'message':message})
		else:
			message = "Relative Order should be in Decreasing Order."
			return render(request, 'Teacher/Teacher_set_final_grade_policy.html', {'context': grade_policy,'message':message})

	else:
		return render(request, 'Teacher/Teacher_set_final_grade_policy.html', {'context':grade_policy,'message':message})



def add_announcements(request,slug):
	if request.method == 'POST':
		x=Teachers.objects.get(slug=slug)
		comment = request.POST['comment']
		date = str(datetime.now())
		obj=Announcements.objects.create(A_tid=x,A_comment=comment,A_date=date)
		obj.save()
		all_comments= Announcements.objects.all()
		all_comments = all_comments[::-1]
		return render(request,'Teacher/Teacher_add_announcements.html',{'ab':all_comments})
	else:
		all_comments= Announcements.objects.all()
		all_comments = all_comments[::-1]
		return render(request,'Teacher/Teacher_add_announcements.html',{'ab':all_comments})




def takeattendance(request,slug):
	message = ""
	a_teacher = Teachers.objects.get(T_id=slug)
	course = a_teacher.T_course_id
	studentlist = course.students_set.all()
	if request.method == "POST":
		message = "Successfully Sent Data."
		date = datetime.strptime(request.POST['datepicker'], '%b %d, %Y').strftime('%Y-%m-%d')
		for student in studentlist:
			present = request.POST[student.S_name]
			temp = DatewiseAttendance.objects.get_or_create(student = student, course=course , date=date, present=int(present))
	dict = {'studentlist':studentlist, 'a_teacher':a_teacher, 'message' : message}
	return render(request,'Teacher/Teacher_attendance.html',dict)

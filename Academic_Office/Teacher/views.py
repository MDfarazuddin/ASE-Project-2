from django.shortcuts import render,redirect
from datetime import datetime
from django.http import HttpResponse

from . models import Teachers,Announcements
from Student.models import Students,Courses,Book,Assignment
from .forms import BookForm

def Teacher_Profile(request,slug):
	# try:
	# 	request.session['T_id']
		a_teacher = Teachers.objects.get(slug=slug)
		return render(request,'Teacher/Teacher_View.html',{"a_teacher":a_teacher})
	# except:
	# 	pass
	# try:
	# 	request.session['A_id']
		# a_teacher = Teachers.objects.get(slug=slug)
		# return render(request,'Teacher/Teacher_View.html',{"a_teacher":a_teacher})
	# except:
		# return HttpResponse('not logged in teacher')
		# pass

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
            return HttpResponse('uploaded')
    else:
        form = BookForm()
    return render(request, 'Teacher/upload_book.html', {
        'form': form
    })


def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return HttpResponse('deleted')


def take_attendance(request,slug):

	class student():
		def __init__(self):
			student_name = ''
			student_id = ''
	a_teacher = Teachers.objects.get(slug=slug)
	course = a_teacher.T_course_id.C_id
	a = Students.objects.all()
	students_name = []
	students_id = []

	for x in a:
		if x.S_courses.filter(C_id = course):
			students_name.append(x.S_name)
			students_id.append(x.S_id)
	dict = {'name':students_name,'id':students_id,'a_teacher':a_teacher}
	return render(request,'Teacher/Teacher_attendance.html',dict)


def add_announcements(request,slug):
	if request.method == 'POST':
		x = Teachers.objects.get(slug=slug)
		comment = request.POST('comment')
		date = str(datetime.now())
		Announcements.objects.create(T_id = x, T_comment=comment, T_date = date)
		tid = Announcements.objects.all()
		return render(request,'Teacher/add_announcements.html', {'ab':tid})
	else:
		tid = Announcements.objects.all()
		return render(request, 'Teacher/add_announcements.html', {'ab': tid})

from django.shortcuts import render,redirect

from django.http import HttpResponse

from . models import Teachers
from Student.models import Students,Courses,Book
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



def Course_contents(request):
	return render(request,'Teacher/Teacher_course_contents.html')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'Teacher/book_list.html', {
        'books': books
    })


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'Teacher/upload_book.html', {
        'form': form
    })


def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')

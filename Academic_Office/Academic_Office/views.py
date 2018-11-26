from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Login_student,Login_teacher,Login_admin
from Student.models import Students
from Teacher.models import Teachers
from Admin.models import Admins

def home(request):
	return render(request,'Academic_Office/Home_page.html')
	
def Student_login(request):
	form = Login_student()
	if request.method == 'POST':
		form=Login_student(request.POST)
		if form.is_valid():
			S_id=form.cleaned_data['S_id'].lower()
			if Students.objects.filter(S_id=S_id).count()==1:
				db=Students.objects.get(S_id=S_id)
				if form.cleaned_data['password']==db.S_password:
					request.session['S_id'] = S_id
					request.session['password'] = db.S_password
					s='/Students/'+S_id
					return HttpResponseRedirect(s)

				else:
					return render(request,'Academic_Office/No_password.html')
			else:
				return render(request,'Academic_Office/No_user.html')
		else:
			return render(request,'Academic_Office/login_student.html',{'form':form,'errs':form.errors})
	else:
		if('S_id' in request.session)&('password' in request.session):
			s='/Students/'+S_id
			return HttpResponseRedirect(s)

		form=Login_student()
	return render(request,'Academic_Office/login_student.html',{'form':form})

def Teacher_login(request):
	form1 = Login_teacher()
	if request.method == 'POST':
		form1=Login_teacher(request.POST)
		if form1.is_valid():
			T_id=form1.cleaned_data['T_id'].lower()
			if Teachers.objects.filter(T_id=T_id).count()==1:
				db=Teachers.objects.get(T_id=T_id)
				if form1.cleaned_data['password']==db.T_password:
					request.session['T_id'] = T_id
					request.session['password'] = db.T_password
					s='/Teachers/'+T_id
					return HttpResponseRedirect(s)

				else:
					return render(request,'Academic_Office/No_password.html')
			else:
				return render(request,'Academic_Office/No_user.html')
		else:
			return render(request,'Academic_Office/login_teacher.html',{'form1':form1,'errs':form1.errors})
	else:
		if('T_id' in request.session)&('password' in request.session):
			s='/Teachers/'+T_id
			return HttpResponseRedirect(s)

		form1=Login_teacher()
	return render(request,'Academic_Office/login_teacher.html',{'form1':form1})


def Admin_login(request):
	form2 = Login_admin()
	if request.method == 'POST':
		form2=Login_admin(request.POST)
		if form2.is_valid():
			A_id=form2.cleaned_data['A_id'].lower()
			if Admins.objects.filter(A_id=A_id).count()==1:
				db=Admins.objects.get(A_id=A_id)
				if form2.cleaned_data['password']==db.A_password:
					request.session['A_id'] = A_id
					request.session['password'] = db.A_password
					s='/Admin/home'
					return HttpResponseRedirect(s)

				else:
					return render(request,'Academic_Office/No_password.html')
			else:
				return render(request,'Academic_Office/No_user.html')
		else:
			return render(request,'Academic_Office/login_admin.html',{'form2':form2,'errs':form2.errors})
	else:
		if('A_id' in request.session)&('password' in request.session):
			s='/Admin/home'
			return HttpResponseRedirect(s)

		form2=Login_admin()
	return render(request,'Academic_Office/login_admin.html',{'form2':form2})


def logout1(request):
	try:
		del request.session['S_id']
		del request.session['password']
	except:
		del request.session['A_id']
		del request.session['password']
	return render(request,'Academic_Office/Home_page.html')

def logout2(request):
	try:
		del request.session['T_id']
		del request.session['password']
	except:
		del request.session['A_id']
		del request.session['password']
	return render(request,'Academic_Office/Home_page.html')

def logout3(request):
	del request.session['A_id']
	del request.session['password']
	return render(request,'Academic_Office/Home_page.html')

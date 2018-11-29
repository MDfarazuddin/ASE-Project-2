from django import forms
from Student.models import Courses
from Teacher.models import *

class Register_student(forms.Form):
    S_name=forms.CharField(max_length='50',widget=forms.TextInput(attrs={'placeholder':'student_name'}))
    S_id=forms.CharField(max_length='10',widget=forms.TextInput(attrs={'placeholder':'username'}))
    S_email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    re_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'re_password'}))
    all_courses = Courses.objects.all()
    CHOICES = []  
    for i in range(len(all_courses)):
        CHOICES.append((i,all_courses[i]))
    multiple_checkboxes = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple)




# class Register_teacher(forms.Form):
#     T_name=forms.CharField(max_length='50',widget=forms.TextInput(attrs={'placeholder':'student_name'}))
#     T_id=forms.CharField(max_length='10',widget=forms.TextInput(attrs={'placeholder':'username'}))
#     T_email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
#     all_courses = Courses.objects.all()
#     CHOICES = []
#     for i in range(len(all_courses)):
#         CHOICES.append((i,all_courses[i]))
#     multiple_checkboxes = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple)
#     password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))
#     re_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'re_password'}))


class Register_teacher(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = ('T_id','T_name','T_email','T_course_id','T_password')

from django import forms
from django.forms import ModelForm

from Student.models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('B_cid','title', 'author', 'pdf', 'cover')
class Attendance_form(forms.Form):
 	date_time = forms.DateTimeField(required=False)

class AddAssignment(ModelForm):
    class Meta:
        model = Assignment
        fields = "__all__"

from django import forms

from Student.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('B_cid','title', 'author', 'pdf', 'cover')
class Attendance_form(forms.Form):
 	date_time = forms.DateTimeField(required=False)
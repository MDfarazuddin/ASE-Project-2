from django import forms

from Student.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('B_cid','title', 'author', 'pdf', 'cover')

from django import forms



class Login_student(forms.Form):
    username=forms.CharField(max_length='10',widget=forms.TextInput(attrs={'placeholder':'username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))

from django import forms

class Login_student(forms.Form):
    S_id=forms.CharField(max_length='10',widget=forms.TextInput(attrs={'placeholder':'username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))

class Login_teacher(forms.Form):
    T_id=forms.CharField(max_length='10',widget=forms.TextInput(attrs={'placeholder':'username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))

class Login_admin(forms.Form):
    A_id=forms.CharField(max_length='10',widget=forms.TextInput(attrs={'placeholder':'username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))

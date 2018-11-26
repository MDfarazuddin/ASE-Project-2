from django import forms


class Register_student(forms.Form):
    S_name=forms.CharField(max_length='50',widget=forms.TextInput(attrs={'placeholder':'student_name'}))
    S_id=forms.CharField(max_length='10',widget=forms.TextInput(attrs={'placeholder':'username'}))
    S_email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    re_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'re_password'}))
    CHOICES = (
        ('1', 'ASE-1'),
        ('2', 'Mathematics 3'),
        ('3', 'Algorithms'),
        ('4','Operating Systems'),
        ('5','DSAA'),
        ('6','Communiction Skills 3'),
    )
    multiple_checkboxes = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple)




class Register_teacher(forms.Form):
    T_name=forms.CharField(max_length='50',widget=forms.TextInput(attrs={'placeholder':'student_name'}))
    T_id=forms.CharField(max_length='10',widget=forms.TextInput(attrs={'placeholder':'username'}))
    T_email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    re_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'re_password'}))

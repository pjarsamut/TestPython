from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    surname = forms.CharField(label='Surname', max_length=100)
    age = forms.IntegerField(label='Age')
    expected_salary = forms.DecimalField(label='Expected Salary', max_digits=10, decimal_places=2)
    education = forms.CharField(label='Education', max_length=100)
    gpa = forms.FloatField(label='GPA')
    birthday = forms.DateField(label='Birthday', widget=forms.DateInput(attrs={'type': 'date'}))
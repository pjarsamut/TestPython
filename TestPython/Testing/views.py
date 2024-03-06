import pandas as pd
from django.shortcuts import render, redirect
from django.http import JsonResponse
from urllib3 import HTTPResponse
from .models import Login
from .form import  RegisterForm
import csv


def upload_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES['excel_file']
        df = pd.read_excel(excel_file)
    for index, row in df.iterrows():
            # Assuming the columns in the Excel file match the fields in YourModel
            Login.objects.update_or_create(
                name=row['Name'],
                surname=row['Surname'],
                age=row['Age'],
                expected_salary=row['Expected Salary'],
                education=row['Education'],
                gpa=row['GPA'],
                birthday=row['Birthday'],
            )

def TestRegister(request):
    data = Login.objects.all()
    return JsonResponse({"data": list(data.values())})


def login_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = RegisterForm()

    return render(request, 'testPython/testing/frontend/Registerform.html', {'form': form})

def export_csv(request):
    response = HTTPResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="entries.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Surname', 'Age', 'Expected Salary', 'Education', 'GPA', 'Birthday'])
    for entry in Login.objects.all():
        writer.writerow([entry.name, entry.surname, entry.age, entry.expected_salary, entry.education, entry.gpa, entry.birthday])

    return response


def summary_view(request):
    entries = Login.objects.all()

    # Search functionality
    query = request.GET.get('q')
    if query:
        entries = entries.filter(name__icontains=query)  # Adjust fields as needed

    # Filtering functionality (example: by age)
    min_age = request.GET.get('min_age')
    max_age = request.GET.get('max_age')
    if min_age and max_age:
        entries = entries.filter(age__range=(min_age, max_age))


    return render(request, 'testPython/summary.html', {'entries': entries})


def RegisterForm(request):
    return render(request, 'RegisterForm.html')

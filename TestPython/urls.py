"""
URL configuration for TestPython project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import summary_view, login_view, export_csv, upload_excel, RegisterForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summary/', summary_view, name='summary-view'),
    path('export-csv/', export_csv, name='export-csv'),
    path('edit/<int:entry_id>/', login_view, name='edit-view'),
    path('delete/<int:entry_id>/', login_view, name='delete-view'),
    path('create/', login_view, name='create-view'),  # Assuming you want a create view
    path('upload-excel/', upload_excel, name='upload-excel'),
    path('registerform/', RegisterForm.as_view(), name='register-form'),  # Assuming RegisterForm is a class-based view
]




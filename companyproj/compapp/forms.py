from django import forms
from .models import *
 
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'date_joined', 'date_of_birth', 'phone_number', 'position']
 
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','start_date', 'end_date', 'amount']

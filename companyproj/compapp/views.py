from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.utils import timezone
from .forms import *

# Create your views here.

def employee_list(request):
    employees = Employee.objects.all().order_by('name')
    return render(request, 'employee_list.html', {'employees': employees})

def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    today = timezone.now().date()
    projects = employee.projects.filter(start_date__lte=today, 
                                        end_date__gte=today  )
    
    #projects = employee.projects.all()
    return render(request, 'employee_detail.html', 
                  {'employee': employee, 'projects': projects})

def employee_engineers(request):
    employees = Employee.objects.filter(position__icontains="engineer")
    return render(request, 'employee_list.html', {'employees': employees})

 
def employee_create(request):
    form = EmployeeForm(request.POST or None)
    c = {
        'form': form,
    }
    if form.is_valid():
        employee = form.save()
        return redirect('employee_detail', employee_id=employee.id)
 
    return render(request, 'add_employee.html', c)
 
def project_create(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    form = ProjectForm(request.POST or None)
    c = {
        'form': form,
        'employee': employee,
    }
    if form.is_valid():
        project = form.save(commit=False)
        project.employee = employee
        project.save()
        return redirect('employee_detail', employee_id=employee.id)
 
    return render(request, 'add_project.html', c)
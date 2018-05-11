from django.shortcuts import render
from .forms import AddEmployee
from django.shortcuts import redirect
from .models import Employees
from datetime import datetime
# Create your views here.


def index(request):
    return render(request, 'employees_app/index.html', {'nbar': 'home'})

# Display Employees:
def employees(request):
    employees_list = Employees.objects.all().order_by('last_name')
    return render(request, 'employees_app/employees.html', {'employees_list': employees_list, 'nbar': 'em'})

# Add Employee:
def add_employee(request):
    if request.method == "POST":
        form = AddEmployee(request.POST)
        if form.is_valid(): # this part makes trouble:
            form.save()
            return redirect('employees_app:employees')
        else:
            return redirect('employees_app:index')
    else:
        form = AddEmployee()
    return render(request, 'employees_app/add_employee.html', {'form': form, 'nbar': 'add_em'})


# Edit Employee:
def edit_employee(request, id):
    employee = Employees.objects.get(id=id)
    if request.method == "POST":
        form = AddEmployee(request.POST, instance=employee)
        if form.is_valid():
            employee.save()
            return redirect('employees_app:employees')
    else:
        form = AddEmployee(instance=employee)
    return render(request, 'employees_app/edit_employee.html', {'form': form})

# Remove Employee:
#def remove_employee(request, id):
#    employee = Employees.objects.id(id=id)
#    employee.delete()
#    return redirect('employees_app:employees')

# 404 Error:
def error404(request):
    return render(request, 'employees_app/404.html', {})

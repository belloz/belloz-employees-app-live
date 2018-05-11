from django.shortcuts import render
from .forms import AddEmployee
from django.shortcuts import redirect
from .models import Employees
from datetime import datetime
# Create your views here.


def index(request):
    return render(request, 'employees_app/index.html', {})

# Display Employees:
def employees(request):
    employees_list = Employees.objects.all().order_by('-last_name')
    return render(request, 'employees_app/employees.html', {'employees_list': employees_list})

# Add Employee:
def add_employee(request):
    if request.method == "POST":
        form = AddEmployee(request.POST)
        if form.is_valid(): # this part makes trouble:
            employee = form
            employee.save()
            return redirect('employees_app:employees')
    else:
        form = AddEmployee()
    return render(request, 'employees_app/add_employee.html', {'form': form})


# Edit Employee:
def edit_employee(request, id):
    employee = Employees.objects.get(id=id)
    if request.method == "POST":
        form = AddEmployee(request.POST, instance=employee)
        if form.is_valid():
            employee = form
            employee.save()
            return redirect('employees_app:edit_employee', id=employee.id)
    else:
        form = AddEmployee(instance=employee)
    return render(request, 'employees_app/edit_employee.html', {'form': form})
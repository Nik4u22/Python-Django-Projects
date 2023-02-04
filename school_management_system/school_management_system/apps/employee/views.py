from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee
from apps.department.models import Department

# Create your views here.
def employee_home(request):
    employees = Employee.objects.all()
    return render(request, "employee/employee_home.html", {
        'employees': employees
    })

# Create your views here.
def add_employee(request):
    
    if request.method=="POST":
        
        # Data Fetching
        employee_name = request.POST.get("employee_name")
        employee_gender = request.POST.get("employee_gender")
        employee_address = request.POST.get("employee_address")
        employee_contact_no = request.POST.get("employee_contact_no")
        employee_designation = request.POST.get("employee_designation")
        employee_department_id = request.POST.get("employee_department")
        department = Department.objects.get(pk=employee_department_id)
        department_name = department.name
        # Create model object and set the data
        employee = Employee()
        employee.name = employee_name
        employee.gender = employee_gender
        employee.address = employee_address
        employee.contact_no = employee_contact_no
        employee.designation = employee_designation
        employee.department_id = employee_department_id
        employee.department_name = department_name
    
        # Save the object
        employee.save()
        
        return redirect("/employee/")
    
    departments = Department.objects.all()
    return render(request, "employee/add_employee.html", {
        'departments': departments
    })

def delete_employee(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    employee.delete()
    return redirect("/employee/")

def get_employee(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    departments = Department.objects.all()
    return render(request, "employee/update_employee.html", {
        'employee': employee,
        'departments': departments
    })
    
def update_employee(request, employee_id):
 
    if request.method == "POST":
        # Data Fetching
        employee_name = request.POST.get("employee_name")
        employee_gender = request.POST.get("employee_gender")
        employee_address = request.POST.get("employee_address")
        employee_contact_no = request.POST.get("employee_contact_no")
        employee_designation = request.POST.get("employee_designation")
        employee_department_id = request.POST.get("employee_department")
        department = Department.objects.get(pk=employee_department_id)
        department_name = department.name
        
        # Create model object and set the data
        employee = Employee.objects.get(pk=employee_id)
        employee.name = employee_name
        employee.gender = employee_gender
        employee.address = employee_address
        employee.contact_no = employee_contact_no
        employee.designation = employee_designation
        employee.department_id = employee_department_id
        employee.department_name = department_name
        
        # Save the object
        employee.save()    
        
        return redirect("/employee/")
 
    
    
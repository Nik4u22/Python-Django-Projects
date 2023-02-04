from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Department

# Create your views here.
def department_home(request):
    departments = Department.objects.all()
    return render(request, "department/department_home.html", {
        'departments': departments
    })

# Create your views here.
def add_department(request):
    if request.method=="POST":
        
        # Data Fetching
        department_name = request.POST.get("department_name")
        
        # Create model object and set the data
        department = Department()
        department.name = department_name
        
        # Save the object
        department.save()
        
        return redirect("/department/")
    return render(request, "department/add_department.html", {})

def delete_department(request, department_id):
    department = Department.objects.get(pk=department_id)
    department.delete()
    return redirect("/department/")

def get_department(request, department_id):
    department = Department.objects.get(pk=department_id)
    return render(request, "department/update_department.html", {
        'department': department
    })
    
def update_department(request, department_id):
    if request.method == "POST":
         # Data Fetching
        department_name = request.POST.get("department_name")
        # Create model object and set the data
        department = Department.objects.get(pk=department_id)
        department.name = department_name
        
        # Save the object
        department.save()
    return redirect("/department/")
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from apps.department.models import Department

# Create your views here.
def student_home(request):
    students = Student.objects.all()
    return render(request, "student/student_home.html", {
        'students': students
    })

# Create your views here.
def add_student(request):
    
    if request.method=="POST":
        
        # Data Fetching
        student_roll_no =  request.POST.get("student_roll_no")
        student_name = request.POST.get("student_name")
        student_gender = request.POST.get("student_gender")
        student_address = request.POST.get("student_address")
        student_contact_no = request.POST.get("student_contact_no")
        student_academic_year = request.POST.get("student_academic_year")
        student_department_id = request.POST.get("student_department")
        department = Department.objects.get(pk=student_department_id)
        department_name = department.name
        # Create model object and set the data
        student = Student()
        student.roll_no = student_roll_no
        student.name = student_name
        student.gender = student_gender
        student.academic_year = student_academic_year
        student.address = student_address
        student.contact_no = student_contact_no
        student.academic_year = student_academic_year
        student.department_id = student_department_id
        student.department_name = department_name
    
        # Save the object
        student.save()
        
        return redirect("/student/")
    
    departments = Department.objects.all()
    return render(request, "student/add_student.html", {
        'departments': departments
    })

def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect("/student/")

def get_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    departments = Department.objects.all()
    return render(request, "student/update_student.html", {
        'student': student,
        'departments': departments
    })
    
def update_student(request, student_id):
 
    if request.method == "POST":
         # Data Fetching
        # Data Fetching
        student_roll_no =  request.POST.get("student_roll_no")
        student_name = request.POST.get("student_name")
        student_gender = request.POST.get("student_gender")
        student_address = request.POST.get("student_address")
        student_contact_no = request.POST.get("student_contact_no")
        student_academic_year = request.POST.get("student_academic_year")
        student_department_id = request.POST.get("student_department")
        department = Department.objects.get(pk=student_department_id)
        department_name = department.name
        
        
        # Create model object and set the data
        student = Student.objects.get(pk=student_id)
        student.roll_no = student_roll_no
        student.name = student_name
        student.gender = student_gender
        student.academic_year = student_academic_year
        student.address = student_address
        student.contact_no = student_contact_no
        student.academic_year = student_academic_year
        student.department_id = student_department_id
        student.department_name = department_name
    
        # Save the object
        student.save()
        
        return redirect("/student/")
 
    
    
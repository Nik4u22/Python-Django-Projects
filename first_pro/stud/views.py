from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Testimonial

# Create your views here.
def student_home(request):
    students = Student.objects.all()
    return render(request, "stud/stud_home.html", {
        'students': students
    })

# Create your views here.
def add_student(request):
    if request.method=="POST":
        
        # Data Fetching
        stud_roll_no = request.POST.get("stud_roll_no")
        stud_name = request.POST.get("stud_name")
        stud_gender = request.POST.get("stud_gender")
        stud_age = request.POST.get("stud_age")
        stud_address = request.POST.get("stud_address")
        stud_branch = request.POST.get("stud_branch")
        
        # Create model object and set the data
        student = Student()
        student.rollno = stud_roll_no
        student.name = stud_name
        student.gender = stud_gender
        student.age = stud_age
        student.address = stud_address
        student.branch = stud_branch
        student.is_active = True
        
        # Save the object
        student.save()
        
        return redirect("/stud/home/")
    return render(request, "stud/add_student.html", {})

def delete_student(request, stud_id):
    student = Student.objects.get(pk=stud_id)
    student.delete()
    return redirect("/stud/home/")

def get_student(request, stud_id):
    student = Student.objects.get(pk=stud_id)
    return render(request, "stud/update_student.html", {
        'student': student
    })
    
def update_student(request, stud_id):
    if request.method == "POST":
         # Data Fetching
        stud_roll_no = request.POST.get("stud_roll_no")
        stud_name = request.POST.get("stud_name")
        stud_gender = request.POST.get("stud_gender")
        stud_age = request.POST.get("stud_age")
        stud_address = request.POST.get("stud_address")
        stud_branch = request.POST.get("stud_branch")
        # Create model object and set the data
        student = Student.objects.get(pk=stud_id)
        student.rollno = stud_roll_no
        student.name = stud_name
        student.gender = stud_gender
        student.age = stud_age
        student.address = stud_address
        student.branch = stud_branch
        student.is_active = True
        # Save the object
        student.save()
    return redirect("/stud/home/")

def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, "stud/testimonials.html", {
        'testimonials': testimonials
    })
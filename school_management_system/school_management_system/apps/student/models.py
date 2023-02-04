from django.db import models
from apps.department.models import Department
# Create your models here.
# Create Student Model
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    roll_no = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    address = models.CharField(max_length=150)
    contact_no = models.CharField(max_length=10)
    academic_year = models.CharField(max_length=20)
    added_date = models.DateTimeField(auto_now=True)
    is_active = models.TextField(default=True) 
    department_id = models.CharField(max_length=50)
    department_name = models.CharField(max_length=50)

department = models.ForeignKey(Department, on_delete=models.CASCADE)
 
# To show student name in url
def __str__(self):
    return self.name

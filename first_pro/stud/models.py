from django.db import models

# Create your models here.
class Student(models.Model):
    rollno=models.IntegerField(max_length=10)
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=20)
    age=models.IntegerField(max_length=10)
    address=models.CharField(max_length=200)
    branch=models.CharField(max_length=50)
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    testimonial=models.TextField()
    picture=models.ImageField(upload_to="testimonials/")
    rating=models.IntegerField()
    
    def __str__(self):
        return self.testimonial
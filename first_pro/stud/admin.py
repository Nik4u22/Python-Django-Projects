from django.contrib import admin
from .models import Student, Testimonial
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=('rollno', 'name', 'branch', 'address')
    
admin.site.register(Student, StudentAdmin)
admin.site.register(Testimonial)
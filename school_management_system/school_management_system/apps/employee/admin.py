from django.contrib import admin
from .models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name', 'department_name',)
    
admin.site.register(Employee, EmployeeAdmin)
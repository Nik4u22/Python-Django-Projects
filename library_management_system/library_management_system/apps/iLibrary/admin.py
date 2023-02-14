from django.contrib import admin
from .models import Department, Employee, Student, Book, IssueBook

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', )
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_image', 'name', 'department', 'is_active', )
    
    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_image', 'name', 'department', 'is_active', )
    
    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js')
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_image', 'name', 'author', 'is_issued', )
    
    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js')
    
class IssueBookAdmin(admin.ModelAdmin):
    list_display = ('issue_id', 'book_id', 'issuee_id', 'issue_date', 'renew_date', )
    
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(IssueBook, IssueBookAdmin)
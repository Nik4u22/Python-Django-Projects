from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('home/', student_home),
    path('add-stud/', add_student),
    path('delete-stud/<int:stud_id>', delete_student),
    path('get-stud/<int:stud_id>', get_student),
    path('update-stud/<int:stud_id>', update_student),
    path('testimonials/', testimonials),
]


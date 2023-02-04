from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', student_home),
    path('add-student/', add_student),
    path('delete-student/<int:student_id>', delete_student),
    path('get-student/<int:student_id>', get_student),
    path('update-student/<int:student_id>', update_student),
]


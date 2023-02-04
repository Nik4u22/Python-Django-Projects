from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', employee_home),
    path('add-employee/', add_employee),
    path('delete-employee/<int:employee_id>', delete_employee),
    path('get-employee/<int:employee_id>', get_employee),
    path('update-employee/<int:employee_id>', update_employee),
]


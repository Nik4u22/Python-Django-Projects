from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', department_home),
    path('add-department/', add_department),
    path('delete-department/<int:department_id>', delete_department),
    path('get-department/<int:department_id>', get_department),
    path('update-department/<int:department_id>', update_department),
]


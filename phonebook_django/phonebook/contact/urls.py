from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('login/', loginview, name='login'),
    path('', index, name="index"),
    path('logout/', LogoutView.as_view(next_page="/login/"), name='logout'),
    path('registration/', registration, name='registration'),
    path('create/', create, name='create'),
    path('detail/<int:pk>/', contactBookDetail, name='contactBookDetail'),
    path("search/<str:search_term>/", search, name="search"),
]

from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('login/', user_login, name='login'),
    path('', home, name="home"),
    path('logout/', LogoutView.as_view(next_page="/login/"), name='logout'),
    path('add-book/', add_book, name='add_book'),
    path('delete-book/<int:book_id>/', delete_book, name='delete_book'),
    path('get-book/<int:book_id>/', get_book, name='get_book'),
    path('update-book/<int:book_id>/', update_book, name='update_book'),
    path('issue-book/', issue_book, name='issue_book'),
    path('return-book/', return_book, name='return_book'),
    path('renew-book/', renew_book, name='renew_book'),
    #path("search/<str:search_term>/", search, name="search"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

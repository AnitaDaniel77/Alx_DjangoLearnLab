from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),
]

from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]
from django.urls import path
from .views import add_book, edit_book, delete_book

urlpatterns += [
    path('book/add/', add_book, name='add_book'),
    path('book/edit/<int:pk>/', edit_book, name='edit_book'),
    path('book/delete/<int:pk>/', delete_book, name='delete_book'),
]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>',views.Teacher_Profile,name="T_profile"),
    path('students/<slug:slug>',views.Show_students,name="Show_students"),
    path('C_name/<slug:slug>',views.Course_contents,name="Course_contents"),
    path('C_name/books/upload/', views.upload_book, name='upload_book'),
    path('C_name/books-assignments/list/<slug:slug>', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),

]

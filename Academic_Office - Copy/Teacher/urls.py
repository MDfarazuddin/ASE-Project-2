from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>',views.Teacher_Profile,name="T_profile"),
    path('students/<slug:slug>',views.Show_students,name="Show_students"),
    path('C_name/',views.Course_contents,name="Course_contents")
]

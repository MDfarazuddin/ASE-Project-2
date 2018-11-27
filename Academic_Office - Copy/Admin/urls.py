from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('home/',views.admin_home),
    path('view-profiles/',views.admin_view_profile,name="view_profiles"),
    path('add-teacher/',views.admin_add_teacher,name="add_teacher"),
    path('add-student',views.admin_add_student,name="add_student"),
    path('all/teachers/',views.teacher_list,name="teacher_list"),
    path('all/teachers/',include('Teacher.urls')),
    path('all/students/',views.student_list,name="student_list"),
    path('all/students/',include('Student.urls')),
    path('send-email/<slug:slug>',views.make_email,name="make_email"),
    path('sent-email',views.send_email,name="send_email")
]

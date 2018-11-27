"""Academic_Office URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('login1/',views.Student_login,name='login1'),
    path('logout1/',views.logout1,name='logout1'),
    path('login2/',views.Teacher_login,name='login2'),
    path('logout2/',views.logout2,name='logout2'),
    path('login3/',views.Admin_login,name='login3'),
    path('logout3/',views.logout3,name='logout3'),
    path('Admin/',include('Admin.urls')),
    path('Teachers/',include('Teacher.urls')),
    path('Students/',include('Student.urls')),
]

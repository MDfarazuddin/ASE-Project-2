from . import views
from django.urls import path,include
    

urlpatterns = [
    path('', views.index, name='forum.index'),
    path('result/',views.result,name= 'forum.result')
]

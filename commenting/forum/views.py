from django.shortcuts import render
from django.http import HttpResponse
from .models import Name,Comment
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    name = Name.objects.all()
    comment = Comment.objects.all()

    mylist = zip(name,comment)
    context = {
        'mylist' : mylist,
    }
    return render(request,'forum/index.html', context)


def result(request):
    print("Request Object: {}".format(request.POST))
    name_text = request.POST['name']
    comment = request.POST['comment']
    namelog = Name.objects.create(name_text = name_text)
    commentlog = Comment.objects.create(name_text = namelog, comm_text = comment)

    name = Name.objects.all()
    comment = Comment.objects.all()
    mylist = zip(name,comment)
    context = {
        'mylist' : mylist,
    }

    return render(request,'forum/index.html', context)



        

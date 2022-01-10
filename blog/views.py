from django.shortcuts import HttpResponse, render

# Create your views here.
from . import models


def hello_world(request):
    return HttpResponse('Hello World')


def posts(request):
    post = models.Post.objects.all()
    return render(request, 'post_list.html', {'posts': post})

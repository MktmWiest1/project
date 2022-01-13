from django.shortcuts import render, get_object_or_404
from . import models


def shows_all(request):
    shows = models.TWShows.objects.all()
    return render(request, 'shows_list.html', {'shows': shows})


def show_detail(request,id):
    show = get_object_or_404(models.TWShows, id=id)
    return render(request, 'show_detail.html', {'show': show})


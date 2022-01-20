from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from . import models, forms


def shows_all(request):
    shows = models.TWShows.objects.all()
    return render(request, 'shows_list.html',
                  {'shows': shows})


def shows_detail(request, id):
    show = get_object_or_404(models.TWShows, id=id)
    return render(request, 'show_detail.html',
                  {'show': show})


def add_show(request):
    method = request.method
    if method == 'POST':
        form = forms.ShowsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Show created')
    else:
        form = forms.ShowsForm()
    return render(request, 'add_shows.html', {'form': form})


def show_update(request, id):
    show_object = get_object_or_404(models.TWShows, id=id)
    if request.method == 'POST':
        form = forms.ShowsForm(instance=show_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Show Updated Successfully')
            # return redirect(reverse('shows:show_all'))
    else:
        form = forms.ShowsForm(instance=show_object)
    return render(request, 'show_update.html', {'form': form, 'object': show_object})


def show_delete(request, id):
    show_object = get_object_or_404(models.TVShows, id=id)
    show_object.delete()
    return HttpResponse('Show Deleted')

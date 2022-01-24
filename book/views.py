# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from . import models, forms
from django.views import generic


class BookListViews(generic.ListView):
    template_name = 'book_list.html'
    queryset = models.Book.objects.all()

    def get_quyryset(self):
        return models.Book.objects.filter().order_by("-id")


# def book_list_view(request):
#     books = models.Book.objects.all()
#     return render(request, 'book_list.html', context={'book': books})

class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)


# def books_detail_view(request, id):
#     book = get_object_or_404(models.Book, id=id)
#     return render(request, 'book_detail.html',
#                   {'book': book})

class BookCreateView(generic.CreateView):
    template_name = 'add_book.html'
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = '/book/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateVeiw, self).form_valid(form=form)


# def add_book(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Book created')
#     else:
#         form = forms.BookForm()
#     return render(request, 'add_book.html', {'form': form})
class BookUpdateView(generic.UpdateView):
    template_name = 'show_update.html'
    form_class = forms.BookForm
    success_url = '/book/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)

    def form_valid(self, form):
        return super(BookUpdateView, self).form_valid(form=form)


# def book_update(request, id):
#     book_object = get_object_or_404(models.Book, id=id)
#     if request.method == 'POST':
#         form = forms.BookForm(instance=book_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Book Updated Successfully')
#             # return redirect(reverse('shows:show_all'))
#     else:
#         form = forms.BookForm(instance=book_object)
#     return render(request, 'show_update.html', {'form': form, 'object': book_object})


class BookDeleteView(generic.DeleteView):
    template_name = 'confirm_delete_book.html'
    success_url = '/book/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)

# def book_delete(request, id):
#     book_object = get_object_or_404(models.Book, id=id)
#     book_object.delete()
#     return HttpResponse('Book Deleted')

# class BookExpertView(generic.ExpertViews):
#     template_name = 'book_detail.html'
    # success_url = '/book/'








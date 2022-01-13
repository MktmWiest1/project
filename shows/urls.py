from django.urls import path
from . import views

urlpatterns = [
    path('shows/', views.shows_all, name='shows_all'),
    path('shows/<int:id>/', views.show_detail, name='shows_all'),

]

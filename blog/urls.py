from . import views
from django.urls import path
urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('posts/', views.posts, name='posts'),

]

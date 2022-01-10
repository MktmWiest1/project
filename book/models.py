from django.db import models


class Post1(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


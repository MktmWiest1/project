
from django.db import models


class Book(models.Model):
    GENGER_CHOICE = (
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Romantic', 'Romantic'),
        ('Anime', 'Anime')
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    quantity = models.IntegerField()
    genre = models.CharField(choices=GENGER_CHOICE, max_length=100)
    data_filmed = models.DateField(auto_now_add=True)

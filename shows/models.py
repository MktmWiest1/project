from django.db import models


class TWShows(models.Model):
    GENGER_CHOICE = (
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Romantic', 'Romantic'),
        ('Anime', 'Anime')
    )
    title = models.CharField(max_length=100)
    descrption = models.TextField()
    image = models.ImageField(upload_to='')
    quantity = models.IntegerField()
    genger = models.CharField(choices=GENGER_CHOICE, max_length=100)
    data_filmed = models.DateField()


from django.db import models


class TWShows(models.Model):
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

    def __str__(self):
        return self.title

class ShowComment(models.Model):
    shows = models.ForeignKey(TWShows, on_delete=models.CASCADE,
                            related_name="show_comment")
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.shows.title
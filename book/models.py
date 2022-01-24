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

    def __str__(self):
        return self.title


class BookComment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name="book_comment")
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
         return self.book.title








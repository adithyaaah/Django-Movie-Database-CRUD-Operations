from django.db import models

# Create your models here. 
class Movie(models.Model):
    title = models.CharField(max_length=50, help_text='Enter the title')
    director = models.CharField(max_length=50, help_text='Enter the director\'s name')
    release_date = models.DateField(help_text='enter the released date', null=True)
    genre_choices = [
        ('OTHER', 'Other'),
        ('ACTION', 'Action'),
        ('COMEDY', 'Comedy'),
        ('DRAMA', 'Drama'),
        ('HORROR', 'Horror'),
        ('ROMANCE', 'Romance'),
        ('FICTION', 'Fiction'),
        ('THRILLER', 'Thriller'),
        ('ANIMATION', 'Animation'),
        ('FANTASY', 'Fantasy'),
        ('DOCUMENTARY', 'Documentary'),
    ]
    genre = models.CharField(max_length=50, choices=genre_choices, help_text='select the genre')
    rating_choices = [
        (1, '1 Star'),
        (2, '2 Star'),
        (3, '3 Star'),
        (4, '4 Star'),
        (5, '5 Star'),
    ]
    rating = models.IntegerField(choices=rating_choices, help_text='select the rating', default=3)

    # def __str__(self):
        # return f"{self.title} - {self.director} ({self.release_date}) - {self.get_genre_display()} - {self.get_rating_display()}"
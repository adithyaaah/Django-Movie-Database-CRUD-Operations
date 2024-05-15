# Generated by Django 5.0.6 on 2024-05-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_operation', '0003_alter_movie_genre_alter_movie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, choices=[('ACTION', 'Action'), ('COMEDY', 'Comedy'), ('DRAMA', 'Drama'), ('HORROR', 'Horror'), ('ROMANCE', 'Romance'), ('FICTION', 'Fiction'), ('THRILLER', 'Thriller'), ('ANIMATION', 'Animation'), ('FANTASY', 'Fantasy'), ('DOCUMENTARY', 'Documentary'), ('OTHER', 'Other')], default='OTHER', help_text='select the genre', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, '1 Star'), (2, '2 Star'), (3, '3 Star'), (4, '4 Star'), (5, '5 Star')], default=3, help_text='select the rating', null=True),
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-14 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_operation', '0004_alter_movie_genre_alter_movie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, choices=[('ACTION', 'Action'), ('COMEDY', 'Comedy'), ('DRAMA', 'Drama'), ('HORROR', 'Horror'), ('ROMANCE', 'Romance'), ('FICTION', 'Fiction'), ('THRILLER', 'Thriller'), ('ANIMATION', 'Animation'), ('FANTASY', 'Fantasy'), ('DOCUMENTARY', 'Documentary'), ('OTHER', 'Other')], default='OTHER', help_text='select the genre', max_length=50),
        ),
    ]

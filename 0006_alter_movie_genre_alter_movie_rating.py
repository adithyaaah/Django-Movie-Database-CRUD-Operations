# Generated by Django 5.0.6 on 2024-05-14 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_operation', '0005_alter_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('ACTION', 'Action'), ('COMEDY', 'Comedy'), ('DRAMA', 'Drama'), ('HORROR', 'Horror'), ('ROMANCE', 'Romance'), ('FICTION', 'Fiction'), ('THRILLER', 'Thriller'), ('ANIMATION', 'Animation'), ('FANTASY', 'Fantasy'), ('DOCUMENTARY', 'Documentary'), ('OTHER', 'Other')], help_text='select the genre', max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(choices=[(1, '1 Star'), (2, '2 Star'), (3, '3 Star'), (4, '4 Star'), (5, '5 Star')], default=3, help_text='select the rating'),
        ),
    ]

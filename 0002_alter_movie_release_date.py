# Generated by Django 5.0.6 on 2024-05-14 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(blank=True, help_text='enter the released date', null=True),
        ),
    ]

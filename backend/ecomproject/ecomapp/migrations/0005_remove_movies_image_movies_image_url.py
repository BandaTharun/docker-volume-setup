# Generated by Django 4.2.11 on 2024-04-03 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0004_alter_movies_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='image',
        ),
        migrations.AddField(
            model_name='movies',
            name='image_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

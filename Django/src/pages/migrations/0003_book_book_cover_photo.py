# Generated by Django 3.0.3 on 2020-03-16 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200314_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_cover_photo',
            field=models.ImageField(default='no-image-png.png', upload_to='book_covers'),
        ),
    ]

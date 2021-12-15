# Generated by Django 3.2.7 on 2021-12-06 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20211204_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='image',
            field=models.ImageField(upload_to='image', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='image', verbose_name='Постер'),
        ),
        migrations.AlterField(
            model_name='movieshots',
            name='image',
            field=models.ImageField(upload_to='image', verbose_name='Изображение'),
        ),
    ]
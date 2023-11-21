# Generated by Django 4.2.1 on 2023-11-20 21:01

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('where_to_go_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ('order',), 'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.AlterModelOptions(
            name='placeimage',
            options={'ordering': ['image_order'], 'verbose_name': 'Изображение места', 'verbose_name_plural': 'Изображения мест'},
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(verbose_name='Подробное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(verbose_name='Описание (первый абзац)'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_title',
            field=models.CharField(max_length=255, verbose_name='Заголовок описания'),
        ),
        migrations.AlterField(
            model_name='place',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Показывать на карте'),
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.DecimalField(decimal_places=15, max_digits=18, verbose_name='ГЕО Широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.DecimalField(decimal_places=15, max_digits=18, verbose_name='ГЕО Долгота'),
        ),
        migrations.AlterField(
            model_name='place',
            name='map_placeId',
            field=models.CharField(max_length=125, verbose_name='ID места на карте'),
        ),
        migrations.AlterField(
            model_name='place',
            name='map_title',
            field=models.CharField(max_length=125, verbose_name='Название на карте'),
        ),
        migrations.AlterField(
            model_name='place',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядковый номер'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='image',
            field=models.ImageField(upload_to='place_images/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='image_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок изображения'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='where_to_go_app.place', verbose_name='Место'),
        ),
    ]
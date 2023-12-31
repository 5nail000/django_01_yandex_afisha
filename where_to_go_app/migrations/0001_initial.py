# Generated by Django 4.2.6 on 2023-10-18 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('map_title', models.CharField(max_length=125)),
                ('map_placeId', models.CharField(max_length=125)),
                ('description_title', models.CharField(max_length=255)),
                ('description_short', models.TextField()),
                ('description_long', models.TextField()),
                ('latitude', models.DecimalField(decimal_places=15, max_digits=18)),
                ('longitude', models.DecimalField(decimal_places=15, max_digits=18)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='PlaceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='place_images/')),
                ('image_order', models.PositiveIntegerField(default=0)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='where_to_go_app.place')),
            ],
            options={
                'ordering': ['image_order'],
            },
        ),
    ]

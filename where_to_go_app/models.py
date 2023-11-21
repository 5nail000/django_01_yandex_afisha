from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    is_active = models.BooleanField(default=True, verbose_name="Показывать на карте")
    map_title = models.CharField(max_length=125, verbose_name="Название на карте")
    map_placeId = models.CharField(max_length=125, verbose_name="ID места на карте", unique=True)
    description_title = models.CharField(max_length=255, verbose_name="Заголовок описания", unique=True)
    first_description = models.TextField(verbose_name="Описание (первый абзац)", blank=True)
    full_description = HTMLField(verbose_name="Подробное описание", blank=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=15, verbose_name="ГЕО Широта")
    longitude = models.DecimalField(max_digits=18, decimal_places=15, verbose_name="ГЕО Долгота")
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Порядковый номер")

    class Meta:
        ordering = ('order',)
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return self.map_title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE, verbose_name="Место")
    image = models.ImageField(upload_to='place_images/', verbose_name="Изображение")
    image_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
        verbose_name="Порядок изображения"
        )

    def save(self, *args, **kwargs):
        if not self.id:  # Only update image_order for new objects
            max_order = PlaceImage.objects.filter(place=self.place).count()
            self.image_order = max_order + 1 if max_order else 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['image_order',]
        verbose_name = "Изображение места"
        verbose_name_plural = "Изображения мест"

    def __str__(self):
        return f'{self.place.map_title} ({self.image_order})'

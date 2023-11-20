from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    is_active = models.BooleanField(default=True)
    map_title = models.CharField(max_length=125)
    map_placeId = models.CharField(max_length=125)
    description_title = models.CharField(max_length=255)
    description_short = models.TextField()
    description_long = HTMLField()
    latitude = models.DecimalField(max_digits=18, decimal_places=15)
    longitude = models.DecimalField(max_digits=18, decimal_places=15)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.map_title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='place_images/')
    image_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def save(self, *args, **kwargs):
        if not self.id:  # Only update image_order for new objects
            max_order = PlaceImage.objects.filter(place=self.place).count()
            self.image_order = max_order + 1 if max_order else 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['image_order',]

    def __str__(self):
        return f'{self.place.map_title} ({self.image_order})'

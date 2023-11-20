# python manage.py load_place https://github.com/devmanorg/where-to-go-places/raw/master/places/%D0%9F%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BE%D0%BD%20%C2%AB%D0%9A%D0%BE%D1%81%D0%BC%D0%BE%D1%81%C2%BB%20%D0%BD%D0%B0%20%D0%92%D0%94%D0%9D%D0%A5.json

from django.core.management.base import BaseCommand
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from urllib.parse import urlparse

import requests
import tempfile

from where_to_go_app.models import Place, PlaceImage


class Command(BaseCommand):
    help = 'Load data from JSON file from url'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url)
        data = response.json()

        place, _ = Place.objects.get_or_create(
            map_title=data['title'],
            description_title=data['title'],
            description_short=data['description_short'],
            description_long=data['description_long'],
            latitude=data['coordinates']['lat'],
            longitude=data['coordinates']['lng'],
            # Add other fields if necessary
        )

        for img_url in data['imgs']:
            with tempfile.NamedTemporaryFile() as img_temp:
                img_temp.write(requests.get(img_url).content)
                img_temp.flush()

                img_name = urlparse(img_url).path.split('/')[-1]
                img_file = File(img_temp, name=img_name)

                PlaceImage.objects.create(
                    place=place,
                    image=img_file,
                )

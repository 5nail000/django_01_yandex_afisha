import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from .models import Place, PlaceImage


def main_page(request):

    all_places = Place.objects.all()
    features = []
    for place in all_places:
        if place.is_active:
            features.append({
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [place.longitude, place.latitude]},
                "properties": {
                    "title": f'{place.map_title}',
                    "placeId": f'{place.map_placeId}',
                    "detailsUrl": f'places/{place.id}'
                    }
                })
    geojson_data = {
        "type": "FeatureCollection",
        "features": features
        }

    return render(request, 'index.html', {'geojson_data': geojson_data})


def place_info(request, place_id):
    place = Place.objects.get(id=place_id)
    images = place.images.all()
    images_urls = [img.image.url for img in images]
    data = {
        'id': place.id,
        'is_active': place.is_active,
        'map_title': place.map_title,
        'map_placeId': place.map_placeId,
        'title': place.description_title,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'latitude': str(place.latitude),
        'longitude': str(place.longitude),
        'imgs': images_urls,
    }
    return JsonResponse(data)

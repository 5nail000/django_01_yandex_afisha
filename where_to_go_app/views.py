from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Place, PlaceImage


def main_page(request):

    places = Place.objects.all()
    features = []
    for place in places:
        if place.is_active:
            details_url = reverse('place_detail', kwargs={'place_id': place.id})
            features.append({
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [place.longitude, place.latitude]},
                "properties": {
                    "title": place.map_title,
                    "placeId": place.map_placeId,
                    "detailsUrl": details_url
                    }
                })
    geojson = {
        "type": "FeatureCollection",
        "features": features
        }

    return render(request, 'index.html', {'geojson': geojson})


def place_info(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related('images'), id=place_id)
    images = place.images.all()
    images_urls = [img.image.url for img in images]
    place_info = {
        'id': place.id,
        'is_active': place.is_active,
        'map_title': place.map_title,
        'map_placeId': place.map_placeId,
        'title': place.description_title,
        'description_short': place.first_description,
        'description_long': place.full_description,
        'latitude': str(place.latitude),
        'longitude': str(place.longitude),
        'imgs': images_urls,
    }
    return JsonResponse(place_info)

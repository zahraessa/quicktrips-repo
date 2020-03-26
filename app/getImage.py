import time
import json
import requests
from app.getRandomCity import randomCityGenerator


def getCityImage(city):
    from app.models import ProcessedCity
    for processed in ProcessedCity.query.all():
        if processed.city == city:
            country = processed.country
            region = processed.country

    API_KEY = '14972248-16dc6a93fb1171c338a02329c'

    try:
        URL = "https://pixabay.com/api/?key=" + API_KEY + "&q=" + city
        response = requests.request("GET", URL)
        return response.json()['hits'][0]['largeImageURL']
    except:
        try:
            URL = "https://pixabay.com/api/?key=" + API_KEY + "&q=" + region
            response = requests.request("GET", URL)
            return response.json()['hits'][0]['largeImageURL']
        except:
            try:
                URL = "https://pixabay.com/api/?key=" + API_KEY + "&q=" + country
                response = requests.request("GET", URL)
                return response.json()['hits'][0]['largeImageURL']
            except:
                return 'https://images.pexels.com/photos/373912/pexels-photo-373912.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'


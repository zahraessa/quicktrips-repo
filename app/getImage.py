import time
import json
import requests
from app.randomCity import randomCityGenerator


def getCountryId(countryName):
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/countries"

    querystring = {"namePrefix": countryName}

    headers = {
        'x-rapidapi-host': "wft-geo-db.p.rapidapi.com",
        'x-rapidapi-key': "999c2985c6msh57d4cee167153ebp1476fdjsn9614b09d1759"
    }
    time.sleep(1)

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response


def getCountryImage(countryName):
    countryIdJSON = getCountryId(countryName).text
    countryId = json.loads(countryIdJSON)
    code = countryId['data'][0]['code']
    url = ("https://wft-geo-db.p.rapidapi.com/v1/geo/countries/" + code)
    headers = {
        'x-rapidapi-host': "wft-geo-db.p.rapidapi.com",
        'x-rapidapi-key': "999c2985c6msh57d4cee167153ebp1476fdjsn9614b09d1759"
    }
    time.sleep(1)
    response = requests.request("GET", url, headers=headers)

    return response.json()['data']['flagImageUri']


def getCityImage(city):
    API_KEY = '14972248-16dc6a93fb1171c338a02329c'
    URL = "https://pixabay.com/api/?key=" + API_KEY + "&q=" + city
    response = requests.request("GET", URL)
    try:
        return response.json()['hits'][0]['largeImageURL']
    except:
        return 'https://images.pexels.com/photos/373912/pexels-photo-373912.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'


getCountryId('United Kingdom').text

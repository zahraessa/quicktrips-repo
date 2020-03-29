import requests
from time import sleep


def getCityInfo(city):
    url = "https://tripadvisor1.p.rapidapi.com/locations/search"
    querystring = {"limit": 4, "sort": "relevance", "offset": "0", "lang": "en_US",
                   "currency": "USD", "units": "km", "query": city}
    sleep(3)
    try:
        headers = {
            'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
            "x-rapidapi-key": "0df4ebdc3bmsh617d8ede228707ep13f9f3jsn1b4e41ef933d"
        }
        sleep(2)
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response
    except:
        return


def getCityId(city):
    try:
        return getCityInfo(city).json()['data'][0]['result_object']["location_id"]
    except:
        return ""


def getCityDescription(city, region, country):
    try:
         getCityInfo(city).json()['data'][0]['result_object']["geo_description"]
    except:
        try:
            return getCityInfo(region).json()['data'][0]['result_object']["geo_description"]
        except:
            try:
                return getCityInfo(country).json()['data'][0]['result_object']["geo_description"]
            except:
                return (city + " is a great place to visit.")

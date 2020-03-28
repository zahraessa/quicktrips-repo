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
            "x-rapidapi-key": "9cb72a3b19msh9272cdb2d1ae07cp133e32jsnb4dd320937b9"
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
        return getCityInfo(city).json()['data'][0]['result_object']["geo_description"]
    except:
        try:
            return getCityInfo(region).json()['data'][0]['result_object']["geo_description"]
        except:
            try:
                return getCityInfo(country).json()['data'][0]['result_object']["geo_description"]
            except:
                return "A great place to visit"

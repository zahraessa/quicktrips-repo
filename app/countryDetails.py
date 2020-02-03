import requests


def getCountryInfo(country):
    url = "https://tripadvisor1.p.rapidapi.com/locations/search"

    querystring = {"limit": 4, "sort": "relevance", "offset": "0", "lang": "en_US",
                   "currency": "USD", "units": "km", "query": country}

    try:
        headers = {
            'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
            "x-rapidapi-key": "26b3163ca2msh844469326aee594p16a283jsn6ef730a33995"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response
    except:
        headers = {
            'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
            "x-rapidapi-key": "1f79334269mshfc4b60a19d501cep1244f7jsnaf9b5cb281bb"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response


def getCountryId(country):
    try:
        return getCountryInfo(country).json()['data'][0]['result_object']["location_id"]
    except:
        return ""


def getCountryDescription(country):
    try:
        return getCountryInfo(country).json()['data'][0]['result_object']["geo_description"]
    except:
        return ""



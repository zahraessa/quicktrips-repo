import requests


def getCityInfo(city):
    url = "https://tripadvisor1.p.rapidapi.com/locations/search"

    querystring = {"limit": 4, "sort": "relevance", "offset": "0", "lang": "en_US",
                   "currency": "USD", "units": "km", "query": city}

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


def getCityId(city):
    return getCityInfo(city).json()['data'][0]['result_object']["location_id"]


def getCityDescription(city):
    return getCityInfo(city).json()['data'][0]['result_object']["geo_description"]

#the api call limit is 500 calls so I've added extra API keys as a fail safe until we decide on an alternative

def getHotelDetails(city):
    cityid = getCityId(city)
    url = "https://tripadvisor1.p.rapidapi.com/hotels/list"

    querystring = {"pricesmin": "50", "offset": "0", "limit": "4", "nights": "1",
                   "location_id": cityid, "adults": "1", "rooms": "1"}

    try:
        headers = {
            'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
            "x-rapidapi-key": "26b3163ca2msh844469326aee594p16a283jsn6ef730a33995"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        response.json()['data'][0]['photo']['images']['large']['url']
        return response
    except:
        try:
            headers = {
                'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
                "x-rapidapi-key": "1f79334269mshfc4b60a19d501cep1244f7jsnaf9b5cb281bb"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            return response
        except:
            headers = {
                'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
                "x-rapidapi-key": "972ab58325mshaf4cbe07802218fp1fcb76jsn1e3664871862"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            return response



def getHotelName(city, i):
    return getHotelDetails(city).json()['data'][i]['name']


def getHotelPhoto(city, i):
    photo = getHotelDetails(city).json()['data'][i]['photo']['images']['large']['url']
    return photo

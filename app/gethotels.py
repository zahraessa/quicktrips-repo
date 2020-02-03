import requests
from app.cityDetails import getCityId


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
            try:
                headers = {
                    'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
                    "x-rapidapi-key": "972ab58325mshaf4cbe07802218fp1fcb76jsn1e3664871862"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                return response
            except:
                return ""




def getHotelName(city, i):
    try:
        return getHotelDetails(city).json()['data'][i]['name']
    except:
        return ""


def getHotelPhoto(city, i):
    try:
        photo = getHotelDetails(city).json()['data'][i]['photo']['images']['large']['url']
        return photo
    except:
        return ""

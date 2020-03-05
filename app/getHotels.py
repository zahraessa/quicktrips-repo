import requests
from app.getCityDetails import getCityId
from app.getRandomCity import randomCityGenerator


# the api call limit is 500 calls so I've added extra API keys as a fail safe until we decide on an alternative

def getHotelDetails(city, maxbudget, minbudget, adults, childAges, startdate, triplength, currency):
    cityid = getCityId(city)
    print(cityid)
    url = "https://tripadvisor1.p.rapidapi.com/hotels/get-details"

    querystring = {"adults": adults, "nights": triplength, "currency": currency, "lang": "en_US",
                   "child_rm_ages": childAges, "checkin": startdate, "location_id": cityid}

    try:
        headers = {
            'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
            "x-rapidapi-key": "26b3163ca2msh844469326aee594p16a283jsn6ef730a33995"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()
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




a = randomCityGenerator()
try:
    city = a[2]
    print(city)
    # coordinates = getCoordinates(city)
    # print(coordinates)
    response = getHotelDetails(city, "10000", "300", "2", "7%2C10", "2020-06-08", "2", "USD")
    print(response.text)
    if response.json()[1]["status"]["unfiltered_total_size"].__str__:
        print('iiiiiii')
        raise Exception("Invalid")
except:
    county = a[0]
    print(county)
    # coordinates = getCoordinates(city)
    # print(coordinates)
    print(getHotelDetails(county, "10000", "300", "2", "7%2C10", "2020-06-08", "2", "USD"))


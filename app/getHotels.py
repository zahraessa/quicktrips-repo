import requests
from app.getCityDetails import getCityId
from app.getRandomCity import randomCityGenerator
from app.getCityCoordinates import getCoordinates


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
                return "AAAA"


def getHotelName(i, text):
    try:
        name = text['data'][i]['name']
        return name
    except:
        return ""


def getHotelPhoto(i, text):
    try:
        photo = text['data'][i]['photo']['images']['large']['url']
        return photo
    except:
        return ""


def getHotelPrice(i, text):
    try:
        price = text['data'][i]['price']
        return price
    except:
        return ""


def getHotelBookingURL(i, text):
    try:
        url = text['data'][i]['web_url']
        return url
    except:
        return ""

def getHotelClass(i, text):
    try:
        hotelClass = text['data'][i]['hotel_class']
        return hotelClass
    except:
        return ""



def getHotelList(city, country, region, maxbudget, minbudget, adults, childAges, startdate, triplength, currency):
    response = ""
    try:
        response = getHotelDetails(city, maxbudget, minbudget, adults, childAges, startdate, triplength, currency)
    except:
        try:
            response = getHotelDetails(region, maxbudget, minbudget, adults, childAges, startdate, triplength, currency)
        except:
            try:
                response = getHotelDetails(country, maxbudget, minbudget, adults, childAges, startdate, triplength, currency)
            except:
                print("NONE")
                return "None found"

    hotels = {}
    for i in range(6):
        try:
            hotels[city] = [getHotelName(i, response), getHotelPhoto(i, response), getHotelBookingURL(i, response),
                            getHotelClass(i, response), getHotelPrice(i, response)]
        except:
            break
    return hotels






origin = "London"
adults = 3
children = 2
numberOfPeople = adults + children
startdate = "2020-05-21"
enddate = "2020-05-25"
currency = "USD"
maxbudget = 10000
minbudget = 0
triplength = 3
keywords = ["family", "wilderness", "food", "warm", "shopping"]

hotels = getHotelList("London", "United Kingdom", "England", maxbudget, minbudget, adults, "", startdate, triplength, currency)

for hotel in hotels:
    print(hotels[hotel])
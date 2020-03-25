import requests
from app.getCityDetails import getCityId
from app.getRandomCity import randomCityGenerator
from app.getCityCoordinates import getCoordinates
from time import sleep


# the api call limit is 500 calls so I've added extra API keys as a fail safe until we decide on an alternative

def generateList(city, maxbudget, minbudget, adults, childAges, startdate, triplength, currency):
    url = "https://tripadvisor1.p.rapidapi.com/hotels/list"
    cityid = getCityId(city)
    querystring = {"zff": "4%2C6", "pricesmin": minbudget, "offset": "0", "subcategory": "hotel%2Cbb%2Cspecialty",
                   "pricesmax": maxbudget, "hotel_class": "1%2C2%2C3", "currency": currency,
                   "amenities": "beach%2Cbar_lounge%2Cairport_transportation", "limit": "10",
                   "checkin": startdate, "order": "asc", "lang": "en_US", "sort": "price", "nights": triplength,
                   "location_id": cityid, "adults": adults, "rooms": "2"}

    headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        "x-rapidapi-key": "999c2985c6msh57d4cee167153ebp1476fdjsn9614b09d1759"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    #print(response)
    return response.json()




def getHotelDetails(hotelId, maxbudget, minbudget, adults, childAges, startdate, triplength, currency):

    url = "https://tripadvisor1.p.rapidapi.com/hotels/get-details"

    querystring = {"adults": adults, "nights": triplength, "currency": currency, "lang": "en_US",
                   "child_rm_ages": childAges, "checkin": startdate, "location_id": hotelId}

    try:
        headers = {
            'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
            "x-rapidapi-key": "999c2985c6msh57d4cee167153ebp1476fdjsn9614b09d1759"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()
    except:
        try:
            headers = {
                'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
                "x-rapidapi-key": "999c2985c6msh57d4cee167153ebp1476fdjsn9614b09d1759"
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
                return


def getHotelName(text):
    try:
        name = text["data"][0]["name"]
        return name
    except:
        return ""


def getHotelPhoto(text):
    try:
        photo = text["data"][0]["photo"]["images"]["original"]["url"]
        return photo
    except:
        return ""


def getHotelPrice(text):
    try:
        price = text["data"][0]["price"]
        return price
    except:
        return ""


def getHotelBookingURL(text):
    try:
        print("AAA")
        # print(text["data"][0])
        url = text["data"][0]["hac_offers"]["offers"][0]["link"]
        return url
    except:
        return ""




def getHotelList(city, country, region, maxbudget, minbudget, adults, childAges, startdate, triplength, currency):
    list = []
    try:
        list = generateList(city, maxbudget, minbudget, adults, "", startdate, triplength, currency)
    except:
        try:
            list = generateList(region, maxbudget, minbudget, adults, "", startdate, triplength, currency)
        except:
            try:
                list = generateList(country, maxbudget, minbudget, adults, "", startdate, triplength, currency)
            except:
                #print("NONE")
                return []

    hotels = []

    #print(list)

    if "data" in list:
        for x in list["data"]:
            sleep(4)
            try:
                id = x["location_id"]
                details = getHotelDetails(id, maxbudget, minbudget, adults, "", startdate, triplength, currency)
                name = getHotelName(details)
                price = getHotelPrice(details)
                photo = getHotelPhoto(details)
                url = getHotelBookingURL(details)
                if name == "" or price == "" or photo == "" or url == "":
                    continue
                else:
                    hotels.append([id, name, price, photo, url])

            except:
                continue
            # print("-------------------------------------")
        print(hotels)
        return hotels
    else:
        return ""

import requests
from app.getCityDetails import getCityId
from time import sleep


def generateList(city, maxbudget, minbudget, adults, childAges, startdate, triplength, currency):
    url = "https://tripadvisor1.p.rapidapi.com/hotels/list"
    cityid = getCityId(city)
    querystring = {"zff": "4%2C6", "pricesmin": minbudget, "offset": "0", "subcategory": "hotel%2Cbb%2Cspecialty",
                   "pricesmax": maxbudget, "hotel_class": "1%2C2%2C3", "currency": currency,
                   "amenities": "beach%2Cbar_lounge%2Cairport_transportation", "limit": "4",
                   "checkin": startdate, "order": "asc", "lang": "en_US", "sort": "price", "nights": triplength,
                   "location_id": cityid, "adults": int(adults) + int(childAges), "rooms": "2"}
    headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        "x-rapidapi-key": "0df4ebdc3bmsh617d8ede228707ep13f9f3jsn1b4e41ef933d"
    }
    sleep(2)
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()


def getHotelDetails(hotelId, adults, childAges, startdate, triplength, currency):
    url = "https://tripadvisor1.p.rapidapi.com/hotels/get-details"
    querystring = {"adults": int(adults) + int(childAges), "nights": triplength, "currency": currency, "lang": "en_US",
                   "child_rm_ages": "", "checkin": startdate, "location_id": hotelId}
    try:
        headers = {
            'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
            "x-rapidapi-key": "0df4ebdc3bmsh617d8ede228707ep13f9f3jsn1b4e41ef933d"
        }
        sleep(2)
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()
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
        url = text["data"][0]["hac_offers"]["offers"][0]["link"]
        return url
    except:
        return ""


def getList(city, country, region, maxbudget, minbudget, adults, childAges, startdate, triplength, currency):
    try:
        return generateList(city, maxbudget, minbudget, adults, childAges, startdate, triplength, currency)
    except:
        try:
            return generateList(region, maxbudget, minbudget, adults, childAges, startdate, triplength, currency)
        except:
            try:
                return generateList(country, maxbudget, minbudget, adults, childAges, startdate, triplength, currency)
            except:
                return []


def getHotelList(city, country, region, maxbudget, minbudget, adults, childAges, startdate, triplength, currency):
    list = getList(city, country, region, maxbudget, minbudget, adults, childAges, startdate, triplength, currency)
    hotels = []
    if "data" in list:
        for x in list["data"]:
            sleep(2)
            try:
                id = x["location_id"]
                details = getHotelDetails(id, adults, childAges, startdate, triplength, currency)
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
    return hotels

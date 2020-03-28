import requests
from app.getCityDetails import getCityId
from app.getRandomCity import randomCityGenerator
from app.getCityCoordinates import getCoordinates
from time import sleep


# the api call limit is 500 calls so I've added extra API keys as a fail safe until we decide on an alternative

def generateList(city, maxbudget, minbudget, adults, childAges, startdate, triplength, currency):
    url = "https://tripadvisor1.p.rapidapi.com/hotels/list"
    cityid = getCityId(city)
    # print(city)
    # print(cityid)
    querystring = {"zff": "4%2C6", "pricesmin": minbudget, "offset": "0", "subcategory": "hotel%2Cbb%2Cspecialty",
                   "pricesmax": maxbudget, "hotel_class": "1%2C2%2C3", "currency": currency,
                   "amenities": "beach%2Cbar_lounge%2Cairport_transportation", "limit": "10",
                   "checkin": startdate, "order": "asc", "lang": "en_US", "sort": "price", "nights": triplength,
                   "location_id": cityid, "adults": int(adults)+int(childAges), "rooms": "2"}

    headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        "x-rapidapi-key": "6a8593230emshb307f117bc19b76p164d0cjsnb9fa28ced57e"
    }

    sleep(2)

    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response)
    return response.json()




def getHotelDetails(hotelId, maxbudget, minbudget, adults, childAges, startdate, triplength, currency):

    url = "https://tripadvisor1.p.rapidapi.com/hotels/get-details"

    querystring = {"adults": int(adults)+int(childAges), "nights": triplength, "currency": currency, "lang": "en_US",
                   "child_rm_ages": "", "checkin": startdate, "location_id": hotelId}

    try:
        headers = {
            'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
            "x-rapidapi-key": "6a8593230emshb307f117bc19b76p164d0cjsnb9fa28ced57e"
        }
        sleep(2)

        response = requests.request("GET", url, headers=headers, params=querystring)
        #print(response.json())
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
        # print("PHOPHO")
        photo = text["data"][0]["photo"]["images"]["original"]["url"]
        # print(photo)
        return photo
    except:
        return ""


def getHotelPrice(text):
    try:
        # print("PRI")
        price = text["data"][0]["price"]
        # print(price)
        return price
    except:
        return ""


def getHotelBookingURL(text):
    try:
        # print("AAA")
        # print(text["data"][0])
        url = text["data"][0]["hac_offers"]["offers"][0]["link"]
        return url
    except:
        return ""




def getHotelList(city, country, region, maxbudget, minbudget, adults, childAges, startdate, triplength, currency):

    list = []
    try:
        print("TESTONE - city")
        list = generateList(city, maxbudget, minbudget, adults, childAges, startdate, triplength, currency)
    except:
        try:
            print("TESTTWO - region")
            list = generateList(region, maxbudget, minbudget, adults, childAges, startdate, triplength, currency)
        except:
            try:
                print("TESTTHREE - country")
                list = generateList(country, maxbudget, minbudget, adults, childAges, startdate, triplength, currency)
            except:
                # print("NONE")
                return []

    hotels = []

    # print(list)

    if "data" in list:
        # print("datahoteldataoop")
        for x in list["data"]:
            # print("WAITWAITWAIT")
            sleep(4)
            try:
                print("TRYYYYYY")
                id = x["location_id"]
                details = getHotelDetails(id, maxbudget, minbudget, adults, childAges, startdate, triplength, currency)
                name = getHotelName(details)
                price = getHotelPrice(details)
                photo = getHotelPhoto(details)
                url = getHotelBookingURL(details)
                if name == "" or price == "" or photo == "" or url == "":
                    print("RIPPITYRIP")
                    continue
                else:
                    print("AYYYYYYYYYYY")
                    hotels.append([id, name, price, photo, url])

            except:
                continue
            print("-----------ee--------------------------")
        print("HoTeLs")
        #print(hotels)
        return hotels
    else:
        # print("NOPE-NULL")
        return ""

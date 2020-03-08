import requests
import json

def getFlights():
    url = "https://api.skypicker.com/aggregation_flights"

    PARAMS = {
        "locations": "CZ",
        "v": 3,
        "partner": "picky",
        "date_from": "12/03/2020",
        "date_to": "19/03/2020",
        "return_from": "21/04/2020",
        "return_to": "05/04/2020",
        "fly_from": "BCN",
        "fly_to": "CZ",
        "nights_in_dst_from": 2,
        "nights_in_dst_to": 5,
        "adults": 1,
        "children": 1,

    }

    r = requests.get(url=url, params=PARAMS)
    data = r.text

    print(r.status_code)
    print(r.reason)
    print(r.encoding)

    return data


def checkFlights():
    url = "https://booking-api.skypicker.com/api/v0.1/check_flights"

    PARAMS = {
        "booking_token": "24c20551-d4a1-4536-89d5-1e0944b4fe7c",
        "v": 2,
        "bnum": 2,
        "pnum": 2,
        "affily": "picky_us",
        "currency": "USD"
    }


    r = requests.get(url=url, params=PARAMS)
    data = r.text

    print(r.status_code)
    print(r.reason)
    print(r.encoding)

    return data


print(getFlights())
print(checkFlights())
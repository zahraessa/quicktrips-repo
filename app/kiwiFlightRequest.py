from kw.platform import requests
import requests
from app.getRandomCity import randomCityGenerator
import json



url = "https://tripadvisor1.p.rapidapi.com/airports/search"

def generateClosestAirports(placeArray):
    try:
        querystring = {"locale": "en_US", "query": placeArray[2]}

        headers = {
            'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
            'x-rapidapi-key': "972ab58325mshaf4cbe07802218fp1fcb76jsn1e3664871862"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        if "errors" in response.text:
            raise Exception("Invalid")
        else:
            airports = json.loads(response.text)
            airportCodes = []
            for airport in airports:
                airportCodes.append(airport["code"])
            return airportCodes
    except:
        try:
            querystring = {"locale": "en_US", "query": placeArray[0]}

            headers = {
                'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
                'x-rapidapi-key': "972ab58325mshaf4cbe07802218fp1fcb76jsn1e3664871862"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            if "errors" in response.text:
                raise Exception("Invalid")
            else:
                airports = json.loads(response.text)
                airportCodes = []
                for airport in airports:
                    airportCodes.append(airport["code"])
                return airportCodes
        except:
            querystring = {"locale": "en_US", "query": placeArray[1]}

            headers = {
                'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
                'x-rapidapi-key': "972ab58325mshaf4cbe07802218fp1fcb76jsn1e3664871862"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            if "errors" in response.text:
                raise Exception("Invalid")
            else:
                airports = json.loads(response.text)
                airportCodes = []
                for airport in airports:
                    airportCodes.append(airport["code"])
                return airportCodes

    return "NO AIRPORTS"


def getFlights(fly_from, fly_to, date_from, date_to, return_from, return_to, adults, children, curr, nights_on_trip_from, nights_on_trip_to):
    S = requests.Session()
    url = "https://api.skypicker.com/traveling_salesman"

    PARAMS = {
        "adults": adults,
        "children": children,
        "v": 3,
        "curr": curr,
        "partner": "picky",
        "sort": "price",
        "asc": 1,
        "limit": 3,
        "date_from": date_from,
        "date_to": date_to,
        "return_from": return_from,
        "return_to": return_to,
        "fly_from": "DE",
        "fly_to": "CZ"
    }
    r = S.post(url=url, params=PARAMS)
    data = r.text

    print(r.status_code)
    print(r.reason)
    print(r.encoding)

    return data



def process():
    o = randomCityGenerator()
    d = randomCityGenerator()

    while d == o:
        d = randomCityGenerator()

    originAirports = generateClosestAirports(o)
    print("ORIGINSSSS")
    print(originAirports)
    destinationAirports = generateClosestAirports(d)
    print("DESTINATIONSSS")
    print(destinationAirports)

    if len(destinationAirports) != 0 and len(originAirports) != 0:
        flights = []
        for originAirport in originAirports:
            for destinationAirport in destinationAirports:
                flights.append(getFlights(fly_from=originAirport, fly_to=destinationAirport, date_from="12/11/2020",
                                          date_to="15/11/2020", return_from="19/11/2020", return_to="22/11/2020",
                                          adults=2, children=2, curr="USD", nights_on_trip_from=2, nights_on_trip_to=5))

        for flight in flights:
            print(flight)
    else:
        # TODO: Remove recommendation if has no airports - add to don't visit table in db
        print("REMOVE RECOMMENDATION")
        process()


process()

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

    return "NO AIRPORT"


def getFlights(originAirports, destinationAirports, adults, childAges, startdate, enddate, currency):
    flights = []
    for originAirport in originAirports:
        for destinationAirport in destinationAirports:
            url = "https://tripadvisor1.p.rapidapi.com/flights/create-session"

            querystring = {"dd2": enddate, "currency": currency, "o2": destinationAirport, "d2": originAirport,
                           "ta": adults, "tc": childAges, "d1": destinationAirport, "o1": originAirport,
                           "dd1": startdate}

            headers = {
                'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
                'x-rapidapi-key': "999c2985c6msh57d4cee167153ebp1476fdjsn9614b09d1759"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            print(response.text)
            flights.append(response.json())

    for flight in flights:
        print(flight["summary"]["sh"])



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
    print(len(destinationAirports))
    if len(destinationAirports) != 0 and len(originAirports) != 0:
        getFlights(originAirports, destinationAirports, "2", "7%2C10", "2020-08-20", "2020-08-25", "USD")
    else:
        #TODO: Remove recommendation if has no airports - add to don't visit table in db
        print("REMOVE RECOMMENDATION")
        process()
#
#
#
# process()
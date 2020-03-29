import requests
import json
from time import sleep


def generateClosestAirport(location):
    url = "https://tripadvisor1.p.rapidapi.com/airports/search"
    try:
        querystring = {"locale": "en_US", "query": location}
        headers = {
            'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
            "x-rapidapi-key": "c452bfd43dmsh0916bd1f1375ea3p120b94jsnbda594295b2a"
        }
        sleep(2)
        response = requests.request("GET", url, headers=headers, params=querystring)
        if "errors" in response.text:
            raise Exception("Invalid")
        else:
            airports = json.loads(response.text)
            airportCode = airports[0]["code"]
            return airportCode
    except:
        return "NO AIRPORT"


def createFlightSession(originAirport, destinationAirport, adults, childAges, startdate, enddate, currency):
    flights = []
    url = "https://tripadvisor1.p.rapidapi.com/flights/create-session"
    querystring = {"dd2": enddate, "currency": currency, "o2": destinationAirport, "d2": originAirport,
                   "ta": adults, "tc": childAges, "d1": destinationAirport, "o1": originAirport,
                   "dd1": startdate}
    headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        "x-rapidapi-key": "c452bfd43dmsh0916bd1f1375ea3p120b94jsnbda594295b2a"
    }
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        flights.append([response.json(), originAirport, destinationAirport])
    except:
        pass
    return parseFlightInfo(flights, originAirport, destinationAirport, currency)


def parseFlightInfo(flights, origin, destination, currency):
    searches = []
    if len(flights) > 0:
        for flight in flights:
            try:
                sh = flight[0]["summary"]["sh"]
                sid = flight[0]["search_params"]["sid"]
                f = getFlightPoll(sid, currency)
                for x in parseF(f):
                    searches.append([origin, destination, sh, sid, x])
            except:
                continue
    if len(searches) > 0:
        return getBookingURL(searches)
    return


def getFlightPoll(sid, currency):
    url = "https://tripadvisor1.p.rapidapi.com/flights/poll"
    querystring = {"currency": currency, "n": "6", "ns": "NON_STOP%2CONE_STOP", "so": "PRICE", "o": "0",
                   "sid": sid}
    headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        "x-rapidapi-key": "fdc1bb028dmsh89558dd26d5702bp165be9jsn63c09bee8aeb"
    }
    sleep(5)
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()


def parseF(f):
    flights = []
    price = ""
    hash = ""
    operator = ""
    try:
        for fl in f["itineraries"]:
            for x in fl['l']:
                price = x["pr"]["p"]
                hash = x["id"]
            for y in fl['f']:
                for x in y['l']:
                    depair = x['da']
                    arrair = x['aa']
                    depdt = x['dd']
                    arrdt = x['ad']
                    try:
                        operator = x['od']
                    except:
                        operator = "Multiple Airlines"
                    flights.append([hash, price, depair, arrair, depdt, arrdt, operator])
        return flights
    except:
        return []


def getBookingURL(searches):
    url = "https://tripadvisor1.p.rapidapi.com/flights/get-booking-url"
    headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        "x-rapidapi-key": "fdc1bb028dmsh89558dd26d5702bp165be9jsn63c09bee8aeb"
    }
    bookingURLS = []
    for search in searches:
        try:
            itinerary = search[4][0]
            querystring = {"searchHash": search[2], "Dest": search[1], "id": itinerary, "Orig": search[0],
                           "searchId": search[3]}
            sleep(2)
            response = requests.request("GET", url, headers=headers, params=querystring)
            booking = response.json()["partner_url"]
            bookingURLS.append([search[4], booking])
        except:
            break
    return bookingURLS


def getFlights(origin, city, country, region, numberOfPeople, startdate, enddate, currency, minbudget, maxbudget):
    originCode = generateClosestAirport(origin)
    destinationCode = generateClosestAirport(region)
    x = []
    if destinationCode != "NO AIRPORT" and originCode != "NO AIRPORT":
        x = createFlightSession(originCode, destinationCode, numberOfPeople, "", startdate, enddate, currency)
    else:
        originCode = generateClosestAirport(origin)
        destinationCode = generateClosestAirport(city)
        if destinationCode != "NO AIRPORT" and originCode != "NO AIRPORT":
            x = createFlightSession(originCode, destinationCode, numberOfPeople, "", startdate, enddate, currency)
        else:
            originCode = generateClosestAirport(origin)
            destinationCode = generateClosestAirport(country)
            if destinationCode != "NO AIRPORT" and originCode != "NO AIRPORT":
                x = createFlightSession(originCode, destinationCode, numberOfPeople, "", startdate, enddate, currency)
            else:
                pass
    if x is not None:
        try:
            for flight in x:
                if (int(flight[0][1]) > int(maxbudget)) or (int(flight[0][1]) < int(minbudget)):
                    x.remove(x.remove(flight))
        except:
            pass
    return x

import requests
from app.getRandomCity import randomCityGenerator
import json


def generateClosestAirport(location):
    url = "https://tripadvisor1.p.rapidapi.com/airports/search"
    try:
        querystring = {"locale": "en_US", "query": location}

        headers = {
            'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
            'x-rapidapi-key': "26b3163ca2msh844469326aee594p16a283jsn6ef730a33995"
        }

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
    searches = []

    #print(originAirport)
    #print(destinationAirport)
    querystring = {"dd2": enddate, "currency": currency, "o2": destinationAirport, "d2": originAirport,
                   "ta": adults, "tc": childAges, "d1": destinationAirport, "o1": originAirport,
                   "dd1": startdate}

    headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        'x-rapidapi-key': "26b3163ca2msh844469326aee594p16a283jsn6ef730a33995"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    #print(response.text)
    try:
        flights.append([response.json(), originAirport, destinationAirport])
    except:
        pass
        #print("AA")

    if len(flights) > 0:
        for flight in flights:
            sh = ""
            sid = ""
            l = ""
            f = []
            try:
                itineraries = []
                sh = flight[0]["summary"]["sh"]
                #print("sh: " + sh)
                sid = flight[0]["search_params"]["sid"]
                #print("sid: " + sid)
                f = getFlightPoll(sid, currency)
                #print(f)
                # print("++++++++++")
                for i in f["itineraries"]:
                    #print("i")
                    #print(i)
                    for j in i["l"]:
                        #print("j")
                        #print(j)
                        x = j["id"]
                        #print("x")
                        #print(x)
                        itineraries.append([x, j["pr"]])
                searches.append([originAirport, destinationAirport, sh, sid, itineraries])

            except:
                pass
                # print(f)
                #print("none")
                #print("BBB")
            #print("-------------------------------------------")
    else:
        # TODO: REMOVE SUGGESTION IF NO FLIGHTS
        #print("No flights available")
        #print("CCC")
        return

    if len(searches) > 0:
        return getBookingURL(searches)
    else:
        # TODO: REMOVE SUGGESTION IF NO FLIGHTS
        #print("REDO")
        return
    return

def getFlightPoll(sid, currency):
    url = "https://tripadvisor1.p.rapidapi.com/flights/poll"

    querystring = {"currency": currency, "n": "6", "ns": "NON_STOP%2CONE_STOP", "so": "PRICE", "o": "0",
                   "sid": sid}

    headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        'x-rapidapi-key': "26b3163ca2msh844469326aee594p16a283jsn6ef730a33995"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()


def getBookingURL(searches):
    url = "https://tripadvisor1.p.rapidapi.com/flights/get-booking-url"
    headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        'x-rapidapi-key': "26b3163ca2msh844469326aee594p16a283jsn6ef730a33995"
    }

    bookingURLS = []

    for search in searches:
        for itinerary in search[4]:
            querystring = {"searchHash": search[2], "Dest": search[1], "id": itinerary[0], "Orig": search[0],
                           "searchId": search[3]}

            response = requests.request("GET", url, headers=headers, params=querystring)
            bookingURLS.append([itinerary[1]['p'], response.json()["partner_url"]])

    try:
        # for u in bookingURLS:
        #     print("URL:")
        #     print(u[1])
        #     print("Price:")
        #     print(u[0])
        return bookingURLS
    except:

        # TODO: Remove recommendation if has no airports - add to don't visit table in db
        print("REMOVE RECOMMENDATION")


def getFlights(origin, destination, country, region, numberOfPeople, startdate, enddate, currency):
    print("-----------------------------------------------------------------------")
    #print(origin)
    #print(destination)
    originCode = generateClosestAirport(origin)
    #print(originCode)
    destinationCode = generateClosestAirport(destination)
    #print(destinationCode)

    if destinationCode != "NO AIRPORT" and originCode != "NO AIRPORT":
        #print("city - FOUND")
        x = createFlightSession(originCode, destinationCode, numberOfPeople, "", startdate, enddate, currency)
        #print(x)
        return x
    else:
        originCode = generateClosestAirport(origin)
        #print(originCode)
        #print(region)
        destinationCode = generateClosestAirport(region)
        #print(destinationCode)
        if destinationCode != "NO AIRPORT" and originCode != "NO AIRPORT":
            #print("region - FOUND")
            x = createFlightSession(originCode, destinationCode, numberOfPeople, "", startdate, enddate, currency)
            #print(x)
            return x
        else:
            originCode = generateClosestAirport(origin)
            #print(originCode)
            destinationCode = generateClosestAirport(country)
            #print(country)
            #print(destinationCode)
            if destinationCode != "NO AIRPORT" and originCode != "NO AIRPORT":
                #print("country - FOUND")
                x = createFlightSession(originCode, destinationCode, numberOfPeople, "", startdate, enddate, currency)
                #print(x)
                return x
            else:
                # TODO: Remove recommendation if has no airports - add to don't visit table in db
                print("REMOVE RECOMMENDATION")
                pass

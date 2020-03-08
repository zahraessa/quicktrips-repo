import requests
from app.getRandomCity import randomCityGenerator
import json


def generateClosestAirports(location):
    url = "https://tripadvisor1.p.rapidapi.com/airports/search"
    try:
        querystring = {"locale": "en_US", "query": location}

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
        return "NO AIRPORT"


def createFlightSession(originAirports, destinationAirports, adults, childAges, startdate, enddate, currency):
    flights = []
    url = "https://tripadvisor1.p.rapidapi.com/flights/create-session"
    searches = []

    for originAirport in originAirports:
        for destinationAirport in destinationAirports:
            querystring = {"dd2": enddate, "currency": currency, "o2": destinationAirport, "d2": originAirport,
                           "ta": adults, "tc": childAges, "d1": destinationAirport, "o1": originAirport,
                           "dd1": startdate}

            headers = {
                'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
                'x-rapidapi-key': "999c2985c6msh57d4cee167153ebp1476fdjsn9614b09d1759"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            # print(response.text)
            try:
                flights.append([response.json(), originAirport, destinationAirport])
            except:
                print("AA")
                return

    if len(flights) > 0:
        for flight in flights:
            sh = ""
            sid = ""
            l = ""
            f = []
            try:
                itineraries = []
                sh = flight[0]["summary"]["sh"]
                # print("sh: " + sh)
                sid = flight[0]["search_params"]["sid"]
                # print("sid: " + sid)
                f = getFlightPoll(sid)
                # print(f)
                # print("++++++++++")
                for i in f["itineraries"]:
                    for j in i["l"]:
                        x = j["id"]
                        itineraries.append([x, j["pr"]])
                searches.append([originAirport, destinationAirport, sh, sid, itineraries])

            except:
                # print(f)
                #print("none")
                print("BBB")
                return
            #print("-------------------------------------------")
    else:
        # TODO: REMOVE SUGGESTION IF NO FLIGHTS
        #print("No flights available")
        print("CCC")
        return

    if len(searches) > 0:
        getBookingURL(searches)
    else:
        # TODO: REMOVE SUGGESTION IF NO FLIGHTS
        print("REDO")


def getFlightPoll(sid):
    url = "https://tripadvisor1.p.rapidapi.com/flights/poll"

    querystring = {"currency": "GBP", "n": "3", "ns": "NON_STOP%2CONE_STOP", "so": "PRICE", "o": "0",
                   "sid": sid}

    headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        'x-rapidapi-key': "999c2985c6msh57d4cee167153ebp1476fdjsn9614b09d1759"
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
        for u in bookingURLS:
            print("URL:")
            print(u[1])
            print("Price:")
            print(u[0])
        return bookingURLS
    except:

        # TODO: Remove recommendation if has no airports - add to don't visit table in db
        print("REMOVE RECOMMENDATION")


def process(originCode, destinationCode):
    o = randomCityGenerator()
    d = randomCityGenerator()

    # print("-----------------------------------------------------------------------")
    originAirports = generateClosestAirports(originCode)
    print(originAirports)
    destinationAirports = generateClosestAirports(destinationCode)
    print(destinationAirports)

    if len(destinationAirports) != 0 and len(originAirports) != 0:
        createFlightSession(originAirports, destinationAirports, "1", "", "2020-04-25", "2020-05-28", "GBP")
    else:
        # TODO: Remove recommendation if has no airports - add to don't visit table in db
        print("REMOVE RECOMMENDATION")


process("Bahrain", "London")


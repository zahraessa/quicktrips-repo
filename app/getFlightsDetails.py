import requests
from app.getRandomCity import randomCityGenerator
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
            #print(airportCode)
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
        "x-rapidapi-key": "c452bfd43dmsh0916bd1f1375ea3p120b94jsnbda594295b2a"
    }

    #print(response.text)
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        #print(response.text)
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
               # print("sh: " + sh)
                sid = flight[0]["search_params"]["sid"]
                #print("sid: " + sid)
                f = getFlightPoll(sid, currency)
                # print("++++++++++")
                #print(f)
                # print(f["itineraries"])
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
                continue
                # print(f)
                # print("none")
                # print("BBB")
            #print("-------------------------------------------")
    else:
        # TODO: REMOVE SUGGESTION IF NO FLIGHTS
        # print("No flights available")
        # print("CCC")
        return

    if len(searches) > 0:
        return getBookingURL(searches)
    else:
        # TODO: REMOVE SUGGESTION IF NO FLIGHTS
        # print("REDO")
        return
    return

def getFlightPoll(sid, currency):
    url = "https://tripadvisor1.p.rapidapi.com/flights/poll"

    querystring = {"currency": currency, "n": "6", "ns": "NON_STOP%2CONE_STOP", "so": "PRICE", "o": "0",
                   "sid": sid}

    headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        "x-rapidapi-key": "fdc1bb028dmsh89558dd26d5702bp165be9jsn63c09bee8aeb"
    }
    sleep(7)
    response = requests.request("GET", url, headers=headers, params=querystring)
    #print(response)
    # print("PLEASE WORK OR I'LL KILL MYSELF")
    # print("TEXTTT")
    # print(response.text)
    # print("JSON")
    # print(response.json())

    return response.json()


def getBookingURL(searches):
    url = "https://tripadvisor1.p.rapidapi.com/flights/get-booking-url"
    headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        "x-rapidapi-key": "fdc1bb028dmsh89558dd26d5702bp165be9jsn63c09bee8aeb"
    }

    bookingURLS = []

    for search in searches:
        # print("LENNNN")
        # print(len(bookingURLS))
        for itinerary in search[4]:
            # print("IIIII")
            #print(itinerary)
            querystring = {"searchHash": search[2], "Dest": search[1], "id": itinerary[0], "Orig": search[0],
                           "searchId": search[3]}

            sleep(2)

            response = requests.request("GET", url, headers=headers, params=querystring)
            print("RPJ")
            try:
                print(response)
                print(response.json())
                price = itinerary[1]['p']
                booking = response.json()["partner_url"]
                # print(price)
                # print(booking)
                bookingURLS.append([price, booking])
            except:
                continue
    #         print("---------------------")
    #     print("++++++++++++++++++++++++")
    #
    # print("OOOOOO")
    # print(len(bookingURLS))

    try:
        # for u in bookingURLS:
        #     print("URL:")
        #     print(u[1])
        #     print("Price:")
        #     print(u[0])
        return bookingURLS
    except:
        return

        # TODO: Remove recommendation if has no airports - add to don't visit table in db
        #print("REMOVE RECOMMENDATION")


def getFlights(origin, city, country, region, numberOfPeople, startdate, enddate, currency):
    # print("-----------------------------------------------------------------------")
    # print(origin)
    # print(destination)
    originCode = generateClosestAirport(origin)
    print(originCode)
    destinationCode = generateClosestAirport(region)
    print(destinationCode)

    if destinationCode != "NO AIRPORT" and originCode != "NO AIRPORT":
        print("city - FOUND")
        x = createFlightSession(originCode, destinationCode, numberOfPeople, "", startdate, enddate, currency)
        #print(x)
        return x
    else:
        originCode = generateClosestAirport(origin)
        #print(originCode)
        #print(region)
        destinationCode = generateClosestAirport(city)
        #print(destinationCode)
        if destinationCode != "NO AIRPORT" and originCode != "NO AIRPORT":
            print("region - FOUND")
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
                print("country - FOUND")
                x = createFlightSession(originCode, destinationCode, numberOfPeople, "", startdate, enddate, currency)
                #print(x)
                return x
            else:
                # TODO: Remove recommendation if has no airports - add to don't visit table in db
                print("REMOVE RECOMMENDATION")
                pass

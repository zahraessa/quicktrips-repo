import requests

url = "https://tripadvisor1.p.rapidapi.com/airports/search"


def generateClosestAirport(placeArray):
    try:
        querystring = {"locale": "en_US", "query": placeArray[2]}

        headers = {
            'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
            "x-rapidapi-key": "9cb72a3b19msh9272cdb2d1ae07cp133e32jsnb4dd320937b9"
        }
        sleep(2)

        response = requests.request("GET", url, headers=headers, params=querystring)

        return(response.text)
    except:
        return "NO AIRPORT"


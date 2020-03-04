import requests

url = "https://tripadvisor1.p.rapidapi.com/airports/search"


def generateClosestAirport(placeArray):
    try:
        querystring = {"locale": "en_US", "query": placeArray[2]}

        headers = {
            'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
            'x-rapidapi-key': "972ab58325mshaf4cbe07802218fp1fcb76jsn1e3664871862"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return(response.text)
    except:
        try:
            querystring = {"locale": "en_US", "query": placeArray[0]}

            headers = {
                'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
                'x-rapidapi-key': "972ab58325mshaf4cbe07802218fp1fcb76jsn1e3664871862"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            return (response.text)
        except:
            querystring = {"locale": "en_US", "query": placeArray[1]}

            headers = {
                'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
                'x-rapidapi-key': "972ab58325mshaf4cbe07802218fp1fcb76jsn1e3664871862"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            return (response.text)

    return "NO AIRPORT"


import requests

url = "https://tripadvisor1.p.rapidapi.com/airports/search"


def generateClosestAirport(placeArray):
    try:
        querystring = {"locale": "en_US", "query": placeArray[2]}

        headers = {
            'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
            "x-rapidapi-key": "7f013bf63emshb796529cfd93ecep1ea3bejsn50d632cc0f0c"
        }
        sleep(2)

        response = requests.request("GET", url, headers=headers, params=querystring)

        return(response.text)
    except:
        try:
            querystring = {"locale": "en_US", "query": placeArray[0]}

            headers = {
                'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
                "x-rapidapi-key": "7f013bf63emshb796529cfd93ecep1ea3bejsn50d632cc0f0c"
            }
            sleep(2)

            response = requests.request("GET", url, headers=headers, params=querystring)

            return (response.text)
        except:
            querystring = {"locale": "en_US", "query": placeArray[1]}

            headers = {
                'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
                "x-rapidapi-key": "7f013bf63emshb796529cfd93ecep1ea3bejsn50d632cc0f0c"
            }

            sleep(2)

            response = requests.request("GET", url, headers=headers, params=querystring)

            return (response.text)

    return "NO AIRPORT"


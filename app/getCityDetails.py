import requests
from time import sleep

def getCityInfo(city):
    url = "https://tripadvisor1.p.rapidapi.com/locations/search"

    querystring = {"limit": 4, "sort": "relevance", "offset": "0", "lang": "en_US",
                   "currency": "USD", "units": "km", "query": city}

    sleep(3)

    try:
        headers = {
            'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
            "x-rapidapi-key": "7f013bf63emshb796529cfd93ecep1ea3bejsn50d632cc0f0c"
        }
        sleep(2)

        response = requests.request("GET", url, headers=headers, params=querystring)
        #print("OLOLOL")
        #print(response.json())
        return response
    except:
        headers = {
            'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
            "x-rapidapi-key": "7f013bf63emshb796529cfd93ecep1ea3bejsn50d632cc0f0c"
        }
        sleep(2)
        response = requests.request("GET", url, headers=headers, params=querystring)
        #print("DDD")
        #print(response)
        return response


def getCityId(city):
    try:
        #print("AAAA")
        x = getCityInfo(city).json()['data'][0]['result_object']["location_id"]
        #print("XX?X")
        #print(x)
        return x
    except:
        #print("N?AN?A")
        return ""


def getCityDescription(city, region, country):
    try:
        #print("HERE")
        x = getCityInfo(city).json()['data'][0]['result_object']["geo_description"]
    except:
        #print("HERE2")
        try:
            #print("HERE3")
            x = getCityInfo(region).json()['data'][0]['result_object']["geo_description"]
        except:
            try:
                #print("HERE4")
                x = getCityInfo(country).json()['data'][0]['result_object']["geo_description"]
            except:
                x = "A great place to visit"
    #print(x)

    return x

import requests
from app.getWikiPage import getWikiPages
from time import sleep

def getURLs(city):
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI"

    querystring = {"autoCorrect":"true","pageNumber":"1","pageSize":"20","q":city,"safeSearch":"true"}

    headers = {
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
        "x-rapidapi-key": "0df4ebdc3bmsh617d8ede228707ep13f9f3jsn1b4e41ef933d"
        }
    sleep(2)
    response = requests.request("GET", url, headers=headers, params=querystring)

    #print(response.text)

    try:
        #print("YUPPPPPP")
        jsonResp = response.json()
    except:
        #print("NOPE")
        return []

    results = []

    results.append(getWikiPages(city))

    for i in range(3):
        try:
            results.append(jsonResp["value"][i]["url"])
        except:
            pass
            # print("No URL")

    querystring = {"autoCorrect": "true", "pageNumber": "1", "pageSize": "20", "q": ("things to do " + city), "safeSearch": "true"}

    headers = {
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
        "x-rapidapi-key": "0df4ebdc3bmsh617d8ede228707ep13f9f3jsn1b4e41ef933d"
    }

    try:
        sleep(2)
        response = requests.request("GET", url, headers=headers, params=querystring)

        jsonResp = response.json()

        for i in range(3):
            #print("xxxxxx")
            try:
                results.append(jsonResp["value"][i]["url"])
            except:
                pass
                #print("No URL")
    except:
        results = []

    #print(results)

    return results

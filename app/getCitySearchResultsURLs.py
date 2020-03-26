import requests
from app.getWikiPage import getWikiPages
from time import sleep

def getURLs(city):
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI"

    querystring = {"autoCorrect":"true","pageNumber":"1","pageSize":"20","q":city,"safeSearch":"true"}

    headers = {
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
        "x-rapidapi-key": "7f013bf63emshb796529cfd93ecep1ea3bejsn50d632cc0f0c"
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
        "x-rapidapi-key": "7f013bf63emshb796529cfd93ecep1ea3bejsn50d632cc0f0c"
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

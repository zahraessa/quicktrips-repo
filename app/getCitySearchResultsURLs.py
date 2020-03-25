import requests
from app.getWikiPage import getWikiPages

def getURLs(city):
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI"

    querystring = {"autoCorrect":"true","pageNumber":"1","pageSize":"20","q":city,"safeSearch":"true"}

    headers = {
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
        'x-rapidapi-key': "972ab58325mshaf4cbe07802218fp1fcb76jsn1e3664871862"
        }

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
        'x-rapidapi-key': "972ab58325mshaf4cbe07802218fp1fcb76jsn1e3664871862"
    }

    try:
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

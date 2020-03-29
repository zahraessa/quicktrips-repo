import requests
from app.getWikiPage import getWikiPages
from time import sleep


def getURLs(city):
    results = []
    results.append(getWikiPages(city))
    querystring = {"autoCorrect": "true", "pageNumber": "1", "pageSize": "20", "q": city, "safeSearch": "true"}
    new_results = URLAPICall(querystring, results)
    querystring = {"autoCorrect": "true", "pageNumber": "1", "pageSize": "20", "q": ("things to do " + city),
                   "safeSearch": "true"}
    return URLAPICall(querystring, new_results)


def URLAPICall(querystring, results):
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI"
    headers = {
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
        "x-rapidapi-key": "0df4ebdc3bmsh617d8ede228707ep13f9f3jsn1b4e41ef933d"
    }
    try:
        sleep(2)
        response = requests.request("GET", url, headers=headers, params=querystring)
        for i in range(3):
            try:
                results.append(response.json()["value"][i]["url"])
            except:
                pass
    except:
        results = []
    return results

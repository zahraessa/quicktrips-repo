import requests

def getWikiPages(city):
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "opensearch",
        "namespace": "0",
        "search": city,
        "limit": "1",
        "format": "json"
    }
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    try:
        url = DATA[3][0]
        return url
    except:
        return DATA[3]

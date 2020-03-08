import requests
import json


def getFlights():

    url = "http://api.wego.com/flights/api/k/2/searches"

    PARAMS = {
              "trips": [
                {
                  "departure_code": "SYD",
                  "arrival_code": "LON",
                  "outbound_date": "2020-05-24",
                  "inbound_date": "2020-05-29"
                }
              ],
              "adults_count": 2,
              "children_count": 1
            }

    r = requests.post(url=url, params=PARAMS)
    print(r.status_code)
    print(r.reason)
    DATA = r

    return DATA


print(getFlights())

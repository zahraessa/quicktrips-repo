from opencage.geocoder import OpenCageGeocode
from pprint import pprint

key = 'b6aadedd567f49069da4bca876d161f4'
geocoder = OpenCageGeocode(key)


def getCityFacts(city):
    return geocoder.geocode(city)
    latitude = cityfactsJSON[0]['annotations']['DMS']['lat'][8:16]
    longitude = cityfactsJSON[0]['annotations']['DMS']['lng'][8:16]
    currency = cityfactsJSON[0]['annotations']['currency']['iso_code']
    flag = cityfactsJSON[0]['annotations']['flag']
    roadside = cityfactsJSON[0]['annotations']['roadinfo']['drive_on']
    roadspeedunit = cityfactsJSON[0]['annotations']['roadinfo']['speed_in']
    timezone = cityfactsJSON[0]['annotations']['timezone']['short_name']

def getCoordinates(city):
    data = getCityFacts(city)
    latitude = data[0]['annotations']['DMS']['lat']
    longitude = data[0]['annotations']['DMS']['lng']
    lat = latitude[0:2]
    lng = longitude[0:2]
    return [lat, lng]


def getCountryCode(city):
    data = getCityFacts(city)
    print(data)
    code = data[0]['components']['country_code']
    return code

print(getCoordinates('London'))
from datapackage import Package
import random

package = Package('https://datahub.io/core/world-cities/datapackage.json')


#generate random cities
def getRandomCities(country):
    cities = {}
    if country == "global":
        for i in range(3):
            try:
                x = randomCityGenerator()
                cities[x[2]] = [x[1], x[0]]
            except:
                x = randomCityGenerator()
                cities[x[2]] = [x[1], x[0]]
    else:
        for i in range(5):
            try:
                x = randomLocalCity(country)
                cities[x[2]] = [x[1], x[0]]
            except:
                x = randomLocalCity(country)
                cities[x[2]] = [x[1], x[0]]

    print(cities)
    return cities





def randomCityGenerator():
    i = random.randint(0, 23016)
    resource = package.resources[1]
    if resource.descriptor['datahub']['type'] == 'derived/csv':
        city = resource.read()[i]
        if not ('Region' in city or 'Province' in city or 'Central' in city or 'South' in city or 'North' in city
                or 'West' in city or 'East' in city or 'N/A' in city) and len(city[2]) > 3:
            return city
        else:
            randomCityGenerator()
    else:
        randomCityGenerator()

        # 0= county
        # 1=country
        # 2=city
        # 3=refnumber


def randomLocalCity(country):
    resource = package.resources[1]
    if resource.descriptor['datahub']['type'] == 'derived/csv':
        filtered = []
        for place in resource.read():
            if place[1] == country:
                filtered.append(place)

        i = random.randint(0, len(filtered)-1)
        return filtered[i]

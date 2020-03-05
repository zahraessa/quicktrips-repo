from datapackage import Package
import random

package = Package('https://datahub.io/core/world-cities/datapackage.json')


def randomCityGenerator():
    i = random.randint(0, 23016)
    resource = package.resources[1]
    if resource.descriptor['datahub']['type'] == 'derived/csv':
        city = resource.read()[i]
        if not ('Region' in city or 'Province' in city or 'Central' in city or 'N/A' in city) and len(city[2]) > 3:
            return city
        else:
            randomCityGenerator()

        # 0= county
        # 1=country
        # 2=city
        # 3=refnumber

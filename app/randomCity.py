from datapackage import Package
import random

package = Package('https://datahub.io/core/world-cities/datapackage.json')


def randomCityGenerator():
    i = random.randint(0, 6000)
    for resource in package.resources:
        if resource.descriptor['datahub']['type'] == 'derived/csv':
            return resource.read()[i]


        #0= county
        #1=country
        #2=city
        #3=refnumber


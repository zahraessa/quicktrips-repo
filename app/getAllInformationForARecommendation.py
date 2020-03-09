from app.generateRecommendation import createRecommendation
from app.getFlightsDetails import getFlights
from app.getHotels import getHotelList
from app.getCityDetails import getCityDescription
from app.getImage import getCityImage


#GET FROM FRONT END FORMS
origin = "London"
adults = 3
children = 2
numberOfPeople = adults + children
startdate = "2020-05-21"
enddate = "2020-05-25"
currency = "USD"
maxbudget = 10000
minbudget = 0
triplength = 3
keywords = ["family", "wilderness", "food", "warm", "shopping"]


def getRecommendationInfo(origin, numberOfPeople, startdate, enddate, currency, triplength, keywords):
    recommendations = {}
    #get cities
    cities = createRecommendation(keywords)

    # get flights and hotels for each city
    for city in cities:
        #print(city)
        region = cities[city]["region"]
        country = cities[city]["country"]
        #TODO: Parse flight JSON
        flights = getFlights(origin, city, country, region, numberOfPeople, startdate, enddate, currency)
        # print("FLIGHTS")
        # print(flights)
        # try:
        #     for flight in flights:
        #         print(flight)
        # except:
        #     print("NO FLIGHTS")
        #TODO: Remove recommendations with errors in hotels / no hotels or flights
        hotels = getHotelList(city, country, region, maxbudget, minbudget, adults, "", startdate, triplength, currency)
        # print("HOTELS")
        # print(hotels)
        # try:
        #     for hotel in hotels:
        #         print(hotel)
        # except:
        #     print("NO HOTELS")
        #TODO: GET DESCRIPTION AND PHOTO FROM COUNTRY/REGION
        description = getCityDescription(city)
        # print("DESCRIPTION")
        # print(description)
        image = getCityImage(city)
        # print("IMAGE")
        # print(image)
        recommendations[city] = [flights, hotels, description, image]

        for x in recommendations:
            print(x)
            print(recommendations[x][0])
            print(recommendations[x][1])
            print(recommendations[x][2])
            print(recommendations[x][3])
            print("-----------------------------")


getRecommendationInfo(origin, numberOfPeople, startdate, enddate, currency, triplength, keywords)
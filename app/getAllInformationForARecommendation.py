from app.generateRecommendation import createRecommendation
from app.getFlightsDetails import getFlights
from app.getHotels import getHotelList
from app.getCityDetails import getCityDescription
from app.getImage import getCityImage
from app.getRandomCity import getRandomCities
from app.models import ProcessedCity


#GET FROM FRONT END FORMS
origin = "Mexico"
adults = 1
children = 1
numberOfPeople = adults + children
startdate = "2020-05-21"
enddate = "2020-05-25"
currency = "USD"
maxbudget = 10000
minbudget = 0
triplength = 3
keywords = ["family", "wilderness", "food", "friends", "shopping"]
localorinternational = "global"


def getRecommendationInfo(origin, numberOfPeople, startdate, enddate, currency, triplength, keywords, localorinternational):
    recommendations = {}
    #print("OOP")
    # generate 20 random cities
    if localorinternational == "local":
        randomCities = getRandomCities(origin)
    else:
        randomCities = getRandomCities("global")
    #filter cities
    cities = createRecommendation(keywords, randomCities)
    flights = []

    # get flights and hotels for each city
    for city in cities:
        #print(city)
        region = cities[city]["region"]
        country = cities[city]["country"]
        #TODO: Parse flight JSON
        flights = getFlights(origin, city, country, region, numberOfPeople, startdate, enddate, currency)
        #print(flights)
        if not flights:
            flights = []
        #print("FLIGHTS")
        #print(flights)
        # try:
        #     for flight in flights:
        #         print(flight)
        # except:
        #     print("NO FLIGHTS")
        #TODO: Remove recommendations with errors in hotels / no hotels or flights
        hotels = getHotelList(city, country, region, maxbudget, minbudget, adults, "", startdate, triplength, currency)
        #print(hotels)
        if not hotels:
            hotels = []
        #print("HOTELS")
        #print(hotels)
        # print("HOTELS")
        # print(hotels)
        # try:
        #     for hotel in hotels:
        #         print(hotel)
        # except:
        #     print("NO HOTELS")
        #TODO: GET DESCRIPTION AND PHOTO FROM COUNTRY/REGION
        processsed = ProcessedCity.query.all()
        for x in processsed:
            if x.city == city:
                description = x.description
                image = x.image
        # print("DESCRIPTION")
        # print(description)
        # print("IMAGE")
        # print(image)
        #TODO: GET MATCHED KEYWORDS
        recommendations[city] = [flights, hotels, description, image, keywords]
    #
    # print("RESULTS")
    # for x in recommendations:
    #     print(x)                      #city
    #     print(recommendations[x][0])  #hotels
    #     print(recommendations[x][1])  #flights
    #     print(recommendations[x][2])  #Description
    #     print(recommendations[x][3])  #Photo
    #     print("-----------------------------")

    return recommendations








#getRecommendationInfo(origin, numberOfPeople, startdate, enddate, currency, triplength, keywords, localorinternational)

from app.generateRecommendation import createRecommendation
from app.getFlightsDetails import getFlights
from app.getHotels import getHotelList
from app.getCityDetails import getCityDescription
from app.getImage import getCityImage
from app.getRandomCity import getRandomCities
from app.models import ProcessedCity


def getRecommendationInfo(origin, adults, children, startdate, enddate, currency, triplength, keywords,
                          localorinternational, maxbudget, minbudget):
    recommendations = {}
    #print("OOP")
    randomCities = []
    # generate 20 random cities
    if localorinternational == "local":
        randomCities = getRandomCities(origin)
    else:
        randomCities = getRandomCities("global")
    #filter cities
    #print("LMNOP")
    cities = createRecommendation(keywords, randomCities)
    flights = []

    #print(cities)

    #print("FOBOBOBOBOFO")
    # get flights and hotels for each city
    for city in cities:
        # print("ZOBOZOBOZOBO")
        # print(city)
        region = cities[city]["region"]
        country = cities[city]["country"]
        #TODO: Parse flight JSON
        # print("FFLLIIGGHHTTSS")
        flights = getFlights(origin, city, country, region, adults+children, startdate, enddate, currency)
        # print(flights)
        if not flights:
            flights = []
        #print("FLIGHTS")222
        #print(flights)
        # try:
        #     for flight in flights:
        #         print(flight)
        # except:
        #     print("NO FLIGHTS")
        #TODO: Remove recommendations with errors in hotels / no hotels or flights
        # print("HHOOTTEELLSS")
        hotels = getHotelList(city, country, region, maxbudget, minbudget, adults, children, startdate, triplength, currency)
        # print(hotels)
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
        # print("DESCRIPTION")
        # print(description)
        # print("IMAGE")
        # print(image)
        #TODO: GET MATCHED KEYWORDS
        recommendations[city] = [flights, hotels, description, keywords]
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

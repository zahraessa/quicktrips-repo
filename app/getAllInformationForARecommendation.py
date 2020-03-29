from app.generateRecommendation import createRecommendation
from app.getFlightsDetails import getFlights
from app.getHotels import getHotelList
from app.getRandomCity import getRandomCities
from app.models import ProcessedCity


def getRecommendationInfo(origin, adults, children, startdate, enddate, currency, triplength, keywords,
                          localorinternational, maxbudget, minbudget):
    recommendations = {}
    if localorinternational == "local":
        randomCities = getRandomCities(origin)
    else:
        randomCities = getRandomCities("global")
    cities = createRecommendation(keywords, randomCities)
    flights = []
    for city in cities:
        region = cities[city]["region"]
        country = cities[city]["country"]
        flights = getFlights(origin, city, country, region, adults+children, startdate, enddate,
                             currency, maxbudget, minbudget)
        if not flights:
            flights = []
        hotels = getHotelList(city, country, region, maxbudget, minbudget, adults, children, startdate, triplength,
                              currency)
        if not hotels:
            hotels = []
        processsed = ProcessedCity.query.all()
        for x in processsed:
            if x.city == city:
                description = x.description
        #TODO: GET MATCHED KEYWORDS
        recommendations[city] = [flights, hotels, description, keywords]
    return recommendations

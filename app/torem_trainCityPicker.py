from app.getRandomCity import getRandomCities
from app.generateRecommendation import createRecommendation


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

def getRecommendationInfo():
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


print(getRecommendationInfo())
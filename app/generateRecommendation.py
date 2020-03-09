from app.getRandomCity import randomCityGenerator
from app.watsonAPICall import getAverageSentiment, getKeywords
from app.keywordsSynonyms import keywords
from app.getCitySearchResultsURLs import getURLs
from app.models import ProcessedCity
from app import app, db


def createRecommendation(formKeywords):
    # generate 20 random cities
    cities = getRandomCities()
    cityStatistics = {}
    # generate 10 urls for each city
    # get sentiment score for each url
    # get keywords from urls
    for city in cities:
        print(city)
        cityKeywords = set()
        averageSentiment = 0
        URLkeywords = []
        cityInDB = db.session.query(ProcessedCity.city).filter_by(city=city).scalar() is not None
        if cityInDB:
            print('true')
            c = db.session.query(ProcessedCity).filter_by(city=city)
            averageSentiment = db.session.query(ProcessedCity.sentiment).filter_by(city=city)
            cityKeywords= db.session.query(ProcessedCity.keywords).filter_by(city=city)
        else:
            print('false')
            urls = getURLs(city)
            averageSentiment = getAverageSentiment(urls)
            watsonKeywords = getKeywords(urls)
            for x in watsonKeywords:
                #print(x)
                for y in keywords:
                    for z in keywords[y]:
                        if z in x:
                            cityKeywords.add(y)
            c = ProcessedCity(city=city, keywords=cityKeywords, sentiment=averageSentiment)
            db.session.add(c)
            db.session.commit()
        matchedKeywords = compareKeywordsToForm(formKeywords, cityKeywords)
        cityStatistics[city] = {'sentiment': averageSentiment, 'keywordsCount': matchedKeywords.__len__(),
                                'keywords': matchedKeywords, 'country': cities[city][0], 'region': cities[city][1]}
        #print(cityStatistics[city])
    return pickRecommendation(cityStatistics)



#generate random cities
def getRandomCities():
    cities = {}
    for i in range(15):
        x = randomCityGenerator()
        #tempCity = randomCityGenerator()[2] --- change back to this for coty using country for testing
        region = x[0] #REGIONN
        country = x[1] #COUNTRYYYY
        city = x[2] #CITYYYY
        cities[city] = [country, region]
    print(cities)
    return cities


# compare keywords from url to words from form
def compareKeywordsToForm(formKeywords, cityKeywords):
    print('compare')
    keywordsCount = 0
    matchedKeywords = set()
    for y in formKeywords:
        for x in cityKeywords:
            if y == x:
                #print(y)
                #print(x)
                keywordsCount += 1
                matchedKeywords.add(x)
    print(keywordsCount)
    return matchedKeywords


def pickRecommendation(citiesdict):
    maxKeywords = 0
    maxcities = []
    maxcitiesdict = {}
    for city in citiesdict:
        print(city)
        keywordCount = citiesdict[city]['keywordsCount']
        sentiment = citiesdict[city]['sentiment']

        if keywordCount > 0 and sentiment > 0.5:
            maxcitiesdict[city] = citiesdict[city].copy()
    print("MAX CITIES")
    for city in maxcitiesdict:
        print(city)
    return maxcitiesdict



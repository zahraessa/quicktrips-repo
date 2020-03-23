from app.getRandomCity import randomCityGenerator
from app.watsonAPICall import getAverageSentiment, getKeywords
from app.keywordsSynonyms import keywords
from app.getCitySearchResultsURLs import getURLs
from app.models import ProcessedCity
from app import app, db


def createRecommend(formKeywords):
    # generate 20 random cities
    cities = getRandomCities()
    cityStatistics = {}
    # generate 10 urls for each city
    # get sentiment score for each url
    # get keywords from urls
    for city in cities:
        print(city)
        averageSentiment = 0
        URLkeywords = []
        cityInDB = db.session.query(ProcessedCity.city).filter_by(city=city).scalar() is not None
        if cityInDB:
            print('true')
            c = db.session.query(ProcessedCity).filter_by(city=city)
            averageSentiment = c.sentiment
            URLkeywords = c.keywords
        else:
            print('false')
            urls = getURLs(city)
            averageSentiment = getAverageSentiment(urls)
            URLkeywords = getKeywords(urls)
            cityKeywords = set()
            for x in URLkeywords:
                for y in keywords:
                    for z in keywords[y]:
                        if z in x:
                            cityKeywords.add(y)

            c = ProcessedCity(city=city, keywords=cityKeywords, sentiment=averageSentiment)
            db.session.add(c)
            db.session.commit()
        matchedKeywords = compareKeywordsToForm(formKeywords, URLkeywords)
        cityStatistics[city] = {'sentiment': averageSentiment, 'keywordsCount': matchedKeywords.__len__(),
                                'keywords': matchedKeywords}
        #print(cityStatistics[city])
    return pickRecommendation(cityStatistics)



#generate random cities
def getRandomCities():
    cities = {}
    for i in range(2):
        #tempCity = randomCityGenerator()[2] --- change back to this for coty using country for testing
        region = randomCityGenerator()[0] #REGIONN
        country = randomCityGenerator()[1] #COUNTRYYYY
        city = randomCityGenerator()[2] #CITYYYY
        cities[city] = [country, region]
    print(cities)
    return cities


# compare keywords from url to words from form
def compareKeywordsToForm(formKeywords, dataKeywords):
    keywordsCount = 0
    matchedKeywords = set()
    for keyword in formKeywords:
        for x in dataKeywords:
            for y in keywords[keyword]:
                if y in x:
                    #print(y)
                    #print(x)
                    keywordsCount += 1
                    matchedKeywords.add(keyword)
    #print(keywordsCount)
    return matchedKeywords


def pickRecommendation(citiesdict):
    maxKeywords = 0
    maxcities = []
    maxcitiesdict = {}
    for city in citiesdict:
        keywordCount = citiesdict[city]['keywordsCount']
        sentiment = citiesdict[city]['sentiment']
        print(city + ": keywords: " + citiesdict[city].get('keywords').__str__())
        print("      keywords count: " + keywordCount.__str__())
        print("      sentiment: " + sentiment.__str__())

        if keywordCount > 2 and sentiment > 0.5:
            maxcitiesdict[city] = citiesdict[city].copy()
    for city in maxcitiesdict:
        print(city)
    return maxcitiesdict


# select recommendation - highest number of keywords + highest sentiment score
#createRecommend(["family", "self drive", "accessible", "cold", "shopping"])

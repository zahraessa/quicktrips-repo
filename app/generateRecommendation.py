from app.generateWatsonAPIData import getAverageSentiment, getKeywords
from app.keywordsSynonyms import keywords
from app.getCitySearchResultsURLs import getURLs
from app.models import ProcessedCity
from app import db
from app.getCityDetails import getCityDescription


def createRecommendation(formKeywords, cities):
    cityStatistics = {}
    for city in cities:
        cityKeywords = set()
        averageSentiment = 0
        processsed = ProcessedCity.query.all()
        found = False
        for x in processsed:
            if x.city == city:
                found = True
                if x.country == cities.get(city)[0]:
                    averageSentiment = x.sentiment
                    cityKeywords = x.keywords
                else:
                    averageSentiment = 0
                    cityKeywords = []
                break
        if not found:
            country = cities.get(city)[0]
            region = cities.get(city)[1]
            newValues = generateNewCityData(city, country, region)
            averageSentiment = newValues[0]
            cityKeywords = newValues[1]
        matchedKeywords = compareKeywordsToForm(formKeywords, cityKeywords)
        cityStatistics[city] = {'sentiment': averageSentiment, 'keywordsCount': matchedKeywords.__len__(),
                                'keywords': matchedKeywords, 'country': cities[city][1], 'region': cities[city][1]}
    return pickRecommendation(cityStatistics)


def generateNewCityData(city, country, region):
    urls = getURLs(city)
    averageSentiment = getAverageSentiment(urls)
    watsonKeywords = getKeywords(urls)
    cityKeywords = set()
    for x in watsonKeywords:
        for y in keywords:
            for z in keywords[y]:
                if z in x:
                    cityKeywords.add(y)
    description = getCityDescription(city, region, country)
    c = ProcessedCity(city=city, country=country, region=region, keywords=cityKeywords,
                      sentiment=averageSentiment, description=description)
    db.session.add(c)
    db.session.commit()
    return [averageSentiment, cityKeywords]


# compare keywords from url to words from form
def compareKeywordsToForm(formKeywords, cityKeywords):
    keywordsCount = 0
    matchedKeywords = set()
    try:
        for y in formKeywords:
            for x in cityKeywords:
                if y == x:
                    keywordsCount += 1
                    matchedKeywords.add(x)
        return matchedKeywords
    except:
        return matchedKeywords


def pickRecommendation(citiesdict):
    maxcitiesdict = {}
    for city in citiesdict:
        keywordCount = citiesdict[city]['keywordsCount']
        sentiment = citiesdict[city]['sentiment']
        if keywordCount > 1 and sentiment > 0.5:
            maxcitiesdict[city] = citiesdict[city].copy()
    return maxcitiesdict



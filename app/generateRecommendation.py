from app.getRandomCity import randomCityGenerator
from app.watsonAPICall import getAverageSentiment, getKeywords
from app.keywordsSynonyms import keywords
from app.getCitySearchResultsURLs import getURLs
from app.models import ProcessedCity
from app import app, db
from app.getImage import getCityImage
from app.getCityDetails import getCityDescription


def createRecommendation(formKeywords, cities):
    # generate 10 urls for each city
    # get sentiment score for each url
    # get keywords from urls
    cityStatistics = {}
    # print("HEREEEEExxxxfxfxfx")
    print(cities)
    for city in cities:
        # print("CCCCC")
        print(city)
        cityKeywords = set()
        averageSentiment = 0
        URLkeywords = []
        processsed = ProcessedCity.query.all()
        found = False
        for x in processsed:
            # print(x)
            # print("PROPPO")
            if x.city == city:
                found = True
                # print(cities.get(city)[0])
                if x.country == cities.get(city)[0]:
                    # print('YASSSSSSS')
                    averageSentiment = x.sentiment
                    cityKeywords = x.keywords
                else:
                    # print('anomaly')
                    averageSentiment = 0
                    cityKeywords = []
                break


        # print(found)
        country = cities.get(city)[0]
        region = cities.get(city)[1]
        if not found:
            print('rip no')
            urls = getURLs(city)
            averageSentiment = getAverageSentiment(urls)
            watsonKeywords = getKeywords(urls)
            for x in watsonKeywords:
                #print(x)
                for y in keywords:
                    for z in keywords[y]:
                        if z in x:
                            cityKeywords.add(y)
            description = getCityDescription(city, region, country)
            c = ProcessedCity(city=city, country=country, region=region, keywords=cityKeywords,
                              sentiment=averageSentiment, description=description)
            db.session.add(c)
            db.session.commit()

        # print("FK")
        # print(formKeywords)
        # print("CK")
        # print(cityKeywords)
        matchedKeywords = compareKeywordsToForm(formKeywords, cityKeywords)
        # print(matchedKeywords)
        cityStatistics[city] = {'sentiment': averageSentiment, 'keywordsCount': matchedKeywords.__len__(),
                                'keywords': matchedKeywords, 'country': cities[city][1], 'region': cities[city][1]}
        # print("stats")
        # print(cityStatistics[city])
    return pickRecommendation(cityStatistics)


# compare keywords from url to words from form
def compareKeywordsToForm(formKeywords, cityKeywords):
    #print('compare')
    keywordsCount = 0
    matchedKeywords = set()
    try:
        for y in formKeywords:
            for x in cityKeywords:
                if y == x:
                    #print(y)
                    #print(x)
                    keywordsCount += 1
                    matchedKeywords.add(x)
        #print(keywordsCount)
        return matchedKeywords
    except:
        return matchedKeywords


def pickRecommendation(citiesdict):
    maxKeywords = 0
    maxcities = []
    maxcitiesdict = {}
    print("PICKY PICKY")
    for city in citiesdict:
        # print(city)
        keywordCount = citiesdict[city]['keywordsCount']
        sentiment = citiesdict[city]['sentiment']
        #print(keywordCount)
        #print(sentiment)
        # print("-----------------")

        if keywordCount > 0 and sentiment > 0.5:
            maxcitiesdict[city] = citiesdict[city].copy()
    print("MAX CITIES")
    for city in maxcitiesdict:
        print(city)
    return maxcitiesdict



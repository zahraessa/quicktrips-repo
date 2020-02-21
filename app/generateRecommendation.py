from app.randomCity import randomCityGenerator
from app.watsondiscoveryfilter import getAverageSentiment, getKeywords
from app.keywordsSynonyms import keywords
from app.getCitySearchResultsURLs import getURLs

def createRecommend(formKeywords):
    # generate 20 random cities
    cities = getRandomCities()
    cityStatistics = {}
    # generate 10 urls for each city
    # get sentiment score for each url
    # get keywords from urls
    for city in cities:
        print(city)
        urls = getURLs(city)
        averageSentiment = getAverageSentiment(urls)
        URLkeywords = getKeywords(urls)
        matchedKeywords = compareKeywordsToForm(formKeywords, URLkeywords)
        cityStatistics[city] = {'sentiment': averageSentiment, 'keywordsCount': matchedKeywords.__len__(),
                                'keywords': matchedKeywords}
        #print(cityStatistics[city])
    return pickRecommendation(cityStatistics)



#generate random cities
def getRandomCities():
    cities = set()
    for i in range(10):
        #tempCity = randomCityGenerator()[2] --- change back to this for coty using country for testing
        #tempCity = randomCityGenerator()[1] #COUNTRYYYY
        tempCity = randomCityGenerator()[2] #CITY   YYYoiuytrfedw   i
        cities.add(tempCity)
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
    print(citiesdict)
    for city in citiesdict:
        keywordCount = citiesdict[city]['keywordsCount']
        sentiment = citiesdict[city]['sentiment']
        print(city + ": keywords: " + keywordCount.__str__())
        print("      sentiment: " + sentiment.__str__())

        if keywordCount > 0 and sentiment > 0.5:
            maxcitiesdict[city] = citiesdict[city].copy()
    for city in maxcitiesdict:
        print(city)
    return maxcitiesdict


# select recommendation - highest number of keywords + highest sentiment score
createRecommend(["family", "self drive", "accessible", "cold", "shopping"])

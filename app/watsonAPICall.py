import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions, EntitiesOptions, KeywordsOptions
from app.getCitySearchResultsURLs import getURLs

authenticator = IAMAuthenticator('S6bZmK-2XVgCTrx8tcayXshYV0rHzx6i94WXUrwvyswE')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator
)


def getAverageSentiment(urls):
    response = ""
    count = 0.0
    sentiment_sum = 0.0

    for url in urls:
        try:
            natural_language_understanding.set_service_url(
                'https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/482ccd18-ba78-4b77'
                '-80b1-5735550f7528')
            response = natural_language_understanding.analyze(
                url=url,
                features=Features(
                    keywords=KeywordsOptions(emotion=True, sentiment=True, limit=3),
                    categories=CategoriesOptions(limit=5))).get_result()
        except:
            pass
            # print(url)
            # print("invalid url")

    for i in range(5):
        try:
            # print(response['keywords'][i]["sentiment"]["score"])
            sentiment_value = float(response['keywords'][i]["sentiment"]["score"])
            if sentiment_value != 0.0:
                count += 1
                sentiment_sum += sentiment_value
        except:
            break

    try:
        return sentiment_sum / count
    except:
        return 0


def getKeywords(urls):
    words = []
    response = ""
    for url in urls:
        try:
            natural_language_understanding.set_service_url(
                'https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/482ccd18-ba78-4b77'
                '-80b1-5735550f7528')
            response = natural_language_understanding.analyze(
                url=url,
                features=Features(
                    keywords=KeywordsOptions(emotion=True, sentiment=True, limit=5),
                    categories=CategoriesOptions(limit=5))).get_result()

            # print(json.dumps(response, indent=2))
        except:
            pass
            # print(url)
            # print("invalid url")
        # print(words)
        for i in range(5):
            try:
                words.append(response['keywords'][i]["text"])
                words.append(response['categories'][i]["label"])
            except:
                break
    return words

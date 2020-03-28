from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions, KeywordsOptions


authenticator = IAMAuthenticator('S8PZIz2Ocql7gm188MRVOrwBdwgh5VT4OvlGgmlnZuWq')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2020-02-24',
    authenticator=authenticator
)

ser_url = 'https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/32a4173a-ec82-4421-b2c4-4b89c6bbd6fb'


def getAverageSentiment(urls):
    response = ""
    count = 0.0
    sentiment_sum = 0.0
    if len(urls) < 0:
        return 0
    for url in urls:
        try:
            natural_language_understanding.set_service_url(ser_url)
            response = natural_language_understanding.analyze(
                url=url,
                features=Features(
                    keywords=KeywordsOptions(emotion=True, sentiment=True, limit=3),
                    categories=CategoriesOptions(limit=5))).get_result()
        except:
            pass
    for i in range(5):
        try:
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
    if len(urls) < 1:
        return words
    for url in urls:
        try:
            natural_language_understanding.set_service_url(ser_url)
            response = natural_language_understanding.analyze(
                url=url,
                features=Features(
                    keywords=KeywordsOptions(emotion=True, sentiment=True, limit=5),
                    categories=CategoriesOptions(limit=5))).get_result()
        except:
            pass
        for i in range(5):
            try:
                words.append(response['keywords'][i]["text"])
                words.append(response['categories'][i]["label"])
            except:
                break
    return words

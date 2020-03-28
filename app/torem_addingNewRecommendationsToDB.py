placejson = randomCityGenerator()
country = placejson[1]
city = placejson[2]
today = date.today()
startdate = today.strftime("%Y/%m/%d")
enddate = "2020/"
currency = "USD"
triplength = "3"
keywords = ["family", "wilderness", "food", "friends", "shopping"]
localorinternational = "global"

new_recommendations = getRecommendationInfo(country, 2, startdate, enddate, currency, triplength, keywords,
                                            localorinternational)

print(len(new_recommendations))

for x in new_recommendations:
    city = x  # city
    hotels = recommendations[x][0]  # hotels
    flights = recommendations[x][1]  # flights
    description = recommendations[x][2]  # Description
    image = recommendations[x][3]  # Photo

    rec = Recommendation(city=city, hotels=hotels, flights=flights, description=description,
                         user_id=user.id)

    db.session.add(rec)
    db.session.commit()

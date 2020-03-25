from app import db
from app.models import ProcessedCity


cities = ProcessedCity.query.all()
print(len(cities))
for city in cities:
    print(city.country)
    print(city.city)
    print(city.keywords)
    print(city.sentiment)
    print(city.image)
    print(city.description)

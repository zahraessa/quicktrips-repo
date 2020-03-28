from app.models import ProcessedCity
from app import db


print(len(ProcessedCity.query.all()))
db.session.query(ProcessedCity).filter(ProcessedCity.description == "A great place to visit").delete()
print(len(ProcessedCity.query.all()))
db.session.commit()
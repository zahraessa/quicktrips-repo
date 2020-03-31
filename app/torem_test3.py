from app.models import Favourite as Favourite
from app import db


print(Favourite.query.all())

# for x in Favourite.query.all():
#     db.session.delete(x)
#     db.session.commit()
#
# print("--------")
# print(Favourite.query.all())
from app.models import Favourite

faves = Favourite.query.all()

for x in faves:
    print(x.city)


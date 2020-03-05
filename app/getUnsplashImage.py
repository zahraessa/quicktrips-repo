from unsplash_search import UnsplashSearch
from app.getRandomCity import randomCityGenerator

unsplash = UnsplashSearch('0ecf885a561e330120c5a13d53ee35e8754bde6a04fde3b2b55b471972179bf6')

def getUnsplashImage(city):
    img = unsplash.search_photo(city) #=> dict
    print(img['img'])


try:
    city = randomCityGenerator()
    print(city)
    getUnsplashImage(city[2])
except:
    print('No image')

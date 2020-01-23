import requests

import requests

url = "https://tripadvisor1.p.rapidapi.com/photos/list"

querystring = {"lang":"en_US","currency":"USD","limit":"50","location_id":"2233968"}

headers = {
    'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
    'x-rapidapi-key': "999c2985c6msh57d4cee167153ebp1476fdjsn9614b09d1759"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)






#
# url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/"
#
# querystring = {"query":"United Kingdom"}
#
# skyscannerheaders = {
#     'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
#     'x-rapidapi-key': "999c2985c6msh57d4cee167153ebp1476fdjsn9614b09d1759"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)
#
#
# querystring = {"query":"United Kingdom"}
#
# googlephotosheaders = {
#   "type": "service_account",
#   "project_id": "quicktrips",
#   "private_key_id": "6fea250835df0b84a2bf8877f94487c11fd55bbe",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQC9WkTOu+BzBJ2+\nK/0b4+BZAD8pnBI7NXm1Cb0zFCNMTheMvN9n3C9+wy0TFNSRdSy/ZNNL5CEsl/Tf\ncR3mxS+cFT7a4FHp/jAnRrAJ4QPGFwGIi6UbXRKhHcHOqvpEbzWd/uUKFcJC7vRY\nLcfM4AXMH7ybX+mhCLemOFfubI03KYTifLpUykzQTQJ3y3ccwNfOb729pODaVKpD\nzjAptWvoEXsn5ZM+Nbwg5uSvqcHGnC3oAhHUJeeEoy08p/2XR6Qc1E4QGtPfNDL/\n/ZBgEGy3SRRv3KVxUbvoHuMifrb0qoIyjwkWK69cy+aN7MoMY91XqFd/8YW5rj1w\nV76DwDCHAgMBAAECggEAErtB0EkHVfQlyKt1q/3PHUQoJhfG4+2RKdFvUoS8+IOc\nfR3YDzWvIHVIBGRh94u7Dqn3jxaKbkIQBXnysSKzktdf3ZYlnvtizG0yj/T0WHMW\ngelSlCeREWLYtSGhMAY9Aca2kK4AsXoNrkVvx6V9B/7hu7scE66W6vjAQMP4n6AD\ne4f9lVAmOfOksGHnJlTPkIxv3UmOS3wted2bs25HT/XBw10sf86bl5UbKceoCbdE\nmo8Hh0Ir38q/deeE0yRrjADmddhuDr7ZlRdajqPldtPAeyYe0l982O3ISsHTV1n3\n+nVEvuI78+Ac1jCE8b1YG52Ayp2RzvIWqPHaToItcQKBgQD3byxAM1BkMmbP5Auf\n45dGfREhe7KMKUAUtiMdOVJkaq7Rbk3F0utxJHVfMnoRm5u007joV8wCagFo66/H\nP4A+4e4K4az/5SriUUMFhp7DMO0F/DLv/0qpKUKM0IHoBZ+z6/OD2muZwS30W8ra\nnnJMTJWq5NqCieYPTITP8YgUVwKBgQDD6Fxxk5Iom502s9eNIvxHwmTkaTguC61z\n3OAnpfmBD3o/Yc2QB+rRUB1pSWZYXgvaMN54volTnAg7XqpvDzZLHn2hVa7tDO87\n+wbEFEtgJI/TIh5XS7nu+UbCPi/STYq0MpdQSeTdxpN8oafgRPpOR3UIfLJy7xSH\n0DXB9NunUQKBgQDRMEVaFcf+nfn8ApGtYK3xYyVLiJfAFdPebsorF95HlUYtO7M2\n74YsBqXQkQ1Qu50deO5YSHnrBJIikTfwHQigoUQuIPOw+J+T7R3bmx+4aDHLoJez\n/cKyV3azNEjPz4lghLhBHjVgLUlb0QskX1bEmO7kJ01xlYJSJuAWKd5hSwKBgQCI\nlGRuok1RljviuTrboLp1ZOdl/p02LNn+Xsy/l4z9F0dJDOx9L6fbyZjXoF6D2P02\nXr+bOmsPKUbr7TGxP8/ASz+WzN+pUE0xae7roKJ0IslKjwzMG3VDT/Ku1SAN5BWB\nT4wCY6H1o82LJECfsDc5f8Pt6NGYI2oSzWvNDuJcIQKBgQCsVT97ymaYmmo+OFMP\n7wfz/selBMlUQIPyrdsXbgfMmnrFaeJ5OEjAdk7NXS9d4HLvVXLB7iBMGZTGnkU9\nJflj2o9pLwWQovlYargGHl5OGK/ynUiFtLDON+ZK+lqrx5oGUHrRhUbza0Y/7QAN\nZzywddkxRBskSIWU9oYbjwlq8w==\n-----END PRIVATE KEY-----\n",
#   "client_email": "quicktrips@quicktrips.iam.gserviceaccount.com",
#   "client_id": "100346262584863575857",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/quicktrips%40quicktrips.iam.gserviceaccount.com"
# }

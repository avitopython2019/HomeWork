from advert import Advert
import json


iphone_str = """{
    "title": "iPhone X",
    "price": 100,
    "location": {
        "address": "город Самара, улица Мориса Тореза, 50",
        "metro_stations": ["Спортивная", "Гагаринская"]
    },
    "number": "89997776655"
    }"""
#"price": 100,
corgi_str = """{
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs",
    "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
    }
}"""

iphone_json = json.loads(iphone_str)
iphone = Advert(iphone_json)

corgi_json = json.loads(corgi_str)
corgi = Advert(corgi_json)

# print(iphone_json)
print(iphone.__dict__)
print(iphone.location.address)

# print(corgi_json)
print(corgi.__dict__)
# print(corgi.location.address)
print(getattr(corgi, "class"))
print(corgi.class_)

import json
import keyword
import sys

class ColorizeMixin():
    repr_color_code = "\033[1;33;40m"
    end_code = "\033[0m"

class Advert(ColorizeMixin, dict):
    price = 0
    def __init__(self, dictionary):
        # super().__init__(dictionary)
        if isinstance(dictionary, dict):
            for key, value in iter(dictionary.items()):
                if not isinstance(value, dict):
                    self[key] = value
                else:
                    self.__setattr__(key, Advert(value))


    def __getattr__(self, attr):
        return self.get(attr)


    def __setattr__(self, key, value):
        self.__setitem__(key, value)


    def __setitem__(self, key, value):
        # super().__setattr__(key, value)
        if keyword.iskeyword(key):
            key = key + "_"
            self.__dict__.update({key: value})
        else:
            self.__dict__.update({key: value})
        if key == 'price' and value < 0:
            raise ValueError("must be >= 0")

    def __repr__(self):
        yellow = self.repr_color_code
        return f'{yellow} {self.title} | {self.price} ₽ {self.end_code}'


corgi_str = """{
  "title": "Вельш-корги",
  "price": 1000,
  "class": "dogs",
  "location": {
    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
  }
}"""

iphone_str = """{
  "title": "iPhone X",
  "price": 100,
  "location": {
    "address": "город Самара, улица Мориса Тореза, 50",
    "metro_stations": ["Спортивная", "Гагаринская"]
  }
}"""


corgi = json.loads(corgi_str)
corgi_ad = Advert(corgi)
print(corgi_ad.class_)
print(corgi_ad.price)

iphone = json.loads(iphone_str)
iphone_ad = Advert(iphone)
# print(iphone_ad.location)
print(iphone_ad.location.metro_stations[0])
print(iphone_ad)
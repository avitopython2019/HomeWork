import json
from Advert import Advert
import pytest


def test_location_address():
    corgi_str = """{
      "title": "Вельш-корги",
      "price": 1000,
      "class": "dogs",
      "location": {
          "address": "поселение Ельдигинское, поселок санатория Тишково, 25"
      }
    }"""
    address = "поселение Ельдигинское, поселок санатория Тишково, 25"
    corgi = json.loads(corgi_str)
    corgi_ad = Advert(corgi)
    assert corgi_ad.location.address == address


def test_without_price():
    lesson_str = """{
    "title": "python",
    "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
        }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.price == 0


def test_minus_price():
    lesson_str = """{
    "title": "python",
    "price": -1,
    "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
        }
    }"""
    lesson = json.loads(lesson_str)
    with pytest.raises(ValueError):
        Advert(lesson)


def test_metro_list():
    iphone_str = """{
    "title": "iPhone X",
    "price": 100,
    "location": {
        "address": "город Самара, улица Мориса Тореза, 50",
        "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }"""
    iphone = json.loads(iphone_str)
    iphone_ad = Advert(iphone)
    assert type(iphone_ad.location.metro_stations) is list


def test_color_attribute():
    iphone_str = """{
    "title": "iPhone X",
    "price": 100,
    "location": {
        "address": "город Самара, улица Мориса Тореза, 50",
        "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }"""
    iphone = json.loads(iphone_str)
    iphone_ad = Advert(iphone)
    assert iphone_ad.repr_color_code == "\033[1;33;40m"

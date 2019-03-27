from advert import Advert
import json
import pytest


corgi_str = """{
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs",
    "location": {
        "address": "сельское поселение Ельдигинское,\
        поселок санатория Тишково, 25"
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


def test_corgi_class():
    corgi_json = json.loads(corgi_str)
    corgi = Advert(corgi_json)
    assert corgi.class_ == corgi_json['class']


def test_iphone_location_address():
    iphone_json = json.loads(iphone_str)
    iphone = Advert(iphone_json)
    assert iphone.location.address == iphone_json['location']['address']


def test_negative_price_exception_ValueError():
    lesson_str = '{"title": "python", "price": -1}'
    lesson_json = json.loads(lesson_str)
    with pytest.raises(ValueError):
        Advert(lesson_json)


def test_none_title_exception_AttributeError():
    lesson_str = '{"price": 100}'
    lesson_json = json.loads(lesson_str)
    with pytest.raises(AttributeError):
        Advert(lesson_json)

def test_not_price():
    lesson_str = '{"title": "python"}'
    lesson_json = json.loads(lesson_str)
    lesson = Advert(lesson_json)
    assert lesson.price == 0

def test_iphone_repr():
    iphone_json = json.loads(iphone_str)
    iphone = Advert(iphone_json)
    assert str(iphone_json['title']) in repr(iphone)\
        and str(iphone_json['price']) in repr(iphone)


def test_iphone_metro_stations_list():
    iphone_json = json.loads(iphone_str)
    iphone = Advert(iphone_json)
    assert type(iphone.location.metro_stations) is list


if __name__ == "__main__":
    corgi_json = json.loads(corgi_str)
    corgi = Advert(corgi_json)
    print(corgi)

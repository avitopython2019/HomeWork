import json

class ObjectFromJson:
    """
    Динамически создаёт атрибуты экземпляра класса из атрибутов JSON-объекта
    """
    def __init__(self, json_dict: dict):
        # print("Hello")
        for k, v in json_dict.items():
            if type(v) is dict:
                self.__setattr__(k, ObjectFromJson(v))
            else:
                self.__setattr__(k, v)

    # def __getattr__(self, item):
    #     raise AttributeError

class Advert:
    """
    Класс представляющий объявление
    """
    def __init__(self, json_dict: dict):
        self.json_obj = ObjectFromJson(json_dict)
        self.title = self.json_obj.title
        if self.json_obj.price <= 0:
            raise ValueError
        self.price = self.json_obj.price

    def __getattr__(self, item):
        #  TODO: если вызовется "location" без других атрибутов через точку,
        #  то вернётся объект. Возможно нужно возвращать словарь
        if item == 'class_':
            return getattr(self.json_obj, 'class')
        return getattr(self.json_obj, item)

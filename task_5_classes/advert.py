import json
import keyword

class ObjectFromJson:
    """
    Динамически создаёт атрибуты экземпляра класса из атрибутов JSON-объекта
    """
    def __init__(self, json_dict: dict):
        for k, v in json_dict.items():
            if type(v) is dict:
                self.__setattr__(k, ObjectFromJson(v))
            else:
                self.__setattr__(k, v)

class ColorizeMixin:
    """
    Миксин, который менять цвет вывода.
    В конструкторе задётся цвет, по-умолчанию цвет - зелёный
    repr_color_text - цвет текста
    repr_bg_color - цвет фона текста
    repr_style_color - стиль текста
    Посмотреть коды можно тут http://ozzmaker.com/add-colour-to-text-in-python/
    """
    repr_color_code = '\033[0;32;48m'
    normal_color_code = '\033[0m'
    def __init__(self,
        repr_color_text = '32',
        repr_bg_color = '48',
        repr_style_color = '0'
        ):
        self.repr_color_code = ''.join([
            '\033[', repr_style_color,
            ';', repr_color_text,
            ';', repr_bg_color, 'm',])
        self.normal_color_code = '\033[0m'


class Advert(ColorizeMixin):
    """
    Класс представляющий объявление
    """
    def __init__(self, json_dict: dict):
        self.json_obj = ObjectFromJson(json_dict)
        self.title = self.json_obj.title
        try:
            self.price = self.json_obj.price
        except AttributeError:
            self.price = 0

        if self.json_obj.price < 0:
            raise ValueError("Price must be >= 0")
        super().__init__()

    def __getattr__(self, item):
        #  TODO: если вызовется "location" без других атрибутов через точку,
        #  то вернётся объект. Возможно нужно возвращать словарь
        if keyword.iskeyword(item[0:-1]):
            return getattr(self.json_obj, item[0:-1])
        return getattr(self.json_obj, item)

    def __repr__(self):
        return super().repr_color_code +\
            f'{self.title} | {self.price} ₽' +\
            super().normal_color_code

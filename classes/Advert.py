import keyword


class ColorizeMixin():
    repr_color_code = "\033[1;33;40m"
    end_code = "\033[0m"


class Advert(ColorizeMixin):
    price = 0

    def __init__(self, dictionary):
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

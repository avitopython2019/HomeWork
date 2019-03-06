import functools
import time
from jsonschema import validate, ValidationError
import validators


def valid(validate_schema):
    """
    Принимает схему валидации ответа запроса
    Возвращает сообщение об ошибке, если валидация не прошла
    """
    def decorator_inner(func: callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ret_val = func(*args, **kwargs)
            try:
                validate(ret_val, schema=validate_schema)
            except ValidationError:
                print("ValidationError! Response is invalid:\n"
                    f"\tSchema: {validate_schema}\n"
                    f"\tResponse: {ret_val}")
                return "Validation if invalid"
            print("Validation success!")
            return ret_val
        return wrapper
    return decorator_inner


def logger(func: callable):
    """
    Декоратор для логгирования входных и выходных параметров функции.
    Пока только в консоль
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ret_val = func(*args, **kwargs)
        print("Call: ", func.__name__)
        print("\targs: ", *args)
        print("\tkwargs: ", kwargs)
        print("\treturn: ", ret_val)
        return ret_val
    return wrapper


cash_dict = {}  # словарь для хранения cash


def cash(ttl):
    """
    Cash decorator.
    Write args of function and return value in cash_dict.
    ttl - time to life, determines how long it takes
    to remove values from cash. one case - one unit of time.
    If ttl == -1 - it mean ttl = infinity
    Кэш декоратор.
    Записывает аргументы функции и возвращаемое значение в cash_dict.
    ttl - время жизни. Определяет как долго хранится кэш данной функции.
    Если ttl == -1 - то данный кэш не стерается.
    """
    def decorator_inner(func: callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            in_out_dict = dict(ttl=ttl, args=args, kwargs=kwargs)
            if len(cash_dict) != 0:
                for k in cash_dict:
                    if k == func.__name__:
                        if args == cash_dict[k]["args"] and kwargs == cash_dict[k]["kwargs"]:
                            return cash_dict[k]["ret_val"]
            ret_val = func(*args, **kwargs)
            if ret_val != None:
                in_out_dict.update({"ret_val":ret_val})
                cash_dict[func.__name__] =  in_out_dict
            temp_cash = cash_dict.copy()
            for k in temp_cash:
                if k != func.__name__:
                    if cash_dict[k]["ttl"] == -1:
                        continue
                    elif cash_dict[k]["ttl"] == 0:
                        del cash_dict[k]
                        continue
                    cash_dict[k]["ttl"] -= 1
            return ret_val
        return wrapper
    return decorator_inner


def time_exec(func : callable):
    """
    Декоратор засекающий время работы функции
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.clock()
        ret_val = func(*args, **kwargs)
        distance_time = time.clock() - start_time
        print(f'Execution time {round(distance_time*1000000, 4)} usec\n')
        return ret_val
    return wrapper


def is_valid_address(address):
    """
    Проверка адреса на валидность
    """
    if not validators.url(address):
        return False
    return True


def is_valid_port(port: int):
    """
    Проверка порта на валидность
    """
    if 1023 < port < 65536:
        return True
    return False


def run_server( addr : str, port : int, *handlers):
    """
    Принимает адрес и порт, проверяет их на валидность
    остальные аргументы функции - кортежи, состоящие из трех элементов:
        (объект_обработчик, (кортеж неименованных переменных), {словарь именнованных})
    аргумент для вызова обработчика без параментров будет выглядеть так : 
            (hangler,(), {})
    """
    if(is_valid_address(addr) and is_valid_port(port) ):
        for func in handlers:
            if len(func) == 3:
                func[0](*func[1], **func[2])
            else:
                print(f"Error: func - {func[0].__name__} doesn't have name or unname args\n")
    else:
        print("Error! Addres or port are invalid!\n")

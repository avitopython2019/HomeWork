import logging
import time
import random

cache_dict = {}
 
def log(func):
    """
    Логируем какая функция вызывается.
    """
    def wrap_log(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
    
        # Открываем файл логов для записи.
        fh = logging.FileHandler("%s.log" % "Server_log")
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        
        logger.info("Вызов функции: %s" % name)
        result = func(*args, **kwargs)
        logger.info("Результат: %s" % result)
        return result
    
    return wrap_log

@log
def random_handlers(list_handler):
    new_list = []
    rand_number = random.randint(1,1000)
    for i in range (1, rand_number):
        val = random.choice(list_handler)
        new_list.append(val)
    return new_list
@log
def start_handlers(num1, num2, handlers_list):
    for handler in handlers_list:
        if handler == "addition":
            addition(num1, num2, handler)
        elif handler == "subtraction":
            subtraction(num1,num2, handler)
        elif handler == "division":
            division(num1,num2, handler)
        elif handler == "multiplication":
            multiplication(num1,num2, handler)
        elif handler == "pow":
            pow(num1,num2, handler)
    return "success"

@log
def run_server(host='http://example.com' , port='30001', *handlers):
    if  port != 30001 or len(handlers) == 0:
        result = f"Неверно задан порт или отсутствуют обработчики."
        print(result)
        return result
    else:
        result = f"Сервер запущен!\n -Порт: {port}\n -Хост: {host}\n"
        print(result)
        return result

def cache(func, cache = cache_dict):
    def decor_func(*args, **kwargs):
        if args in cache:
            print(f"{args[2]}: ({args[0]},{args[1]})")
            print (f"cached value is found {cache[args]}")
            return cache[args]
        else:
            val = func(*args)
            cache[args] = val
            print (f"calculating the value: {val}")
            return val
    return decor_func
    
def time_exec(func):
    def wrap_timer(*args):
        start_time = time.clock()
        ret_val = func(*args)
        distance_time = time.clock() - start_time
        print(f'Execution time {round(distance_time*1000000, 4)} usec\n')
        return ret_val
    return wrap_timer         

@time_exec
@cache
@log
def addition(num1,num2,handler):
    print(f"Adittion: {num1} + {num2}")
    return num1 + num2

@time_exec
@cache
@log
def subtraction(num1,num2,handler):
    print(f"Subtraction: {num1} - {num2}")
    return num1 - num2

@time_exec
@cache
@log
def division(num1,num2,handler):
    print(f"division: {num1} / {num2}")
    try:
        num1/num2
    except ZeroDivisionError:
        return 0
    return num1 / num2

@time_exec
@cache
@log
def multiplication(num1,num2,handler):
    print(f"Multiplication: {num1} * {num2}")
    return num1 * num2

@time_exec
@cache
@log
def pow(num1,num2, handler):
    print(f"Powering: {num1} ** {num2}")
    return num1 ** num2

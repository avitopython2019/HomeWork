import time
from threading import Timer

dictionary_hash = {}
dictionary_log = {}

def add_hash(info):
    dictionary_hash[time.time()] = info
def add_log(info):
    dictionary_log.update([info])

def check_hash():
    for key, value in dictionary_hash.items():

        if(key - time.time() > 10):
            del dictionary_hash[key]
            
def start_hash_timer():
    check_hash()
    t = Timer( 10, start_hash_timer )
    t.start()
    
def find_in_hash(request):
    for key, value in dictionary_hash.items():
        if(value[0] == request):
            return value[1]
    return "not find"

list_handlers = []

def run_server(*args,host,port,config):
    if(len(args) == 0):
        print('Ошибка! Не задано обработчиков.')
    else:
        print('Сервер запущен на хосте {} с портом {}'.format(host, port))

        if('count_thread' in config):
            print('Используется {} поток(а)'.format(config['count_thread']))
        else:
            print('Используется 1 поток')

        for somehandler in args:
            list_handlers.append(somehandler)
            
        #проверка кэша и очистка, временно
        #start_hash_timer()    
        
def request_for_service(request):
    if(len(list_handlers) == 0):
        print('Ошибка! Сервер не запущен')
    else:
        parse_request = ''
        address = ''
        if(request[0] == '/' and request.find(' ') != -1):
            number_elem = request.find(' ')
            parse_request = request[number_elem + 1:]
            address = request[0:number_elem]
            for somehandler in list_handlers:
                if(somehandler('get handler path') == address):
                    somehandler(parse_request)
        else:
            print('Неверный запрос')

def route(path):

    def the_wrapper_around_the_original_function(handler):
        def wrapper_level_2(request):
            if(request == "get handler path"):
                return path
            else:
                then = time.time()
                print('Сервер получил запрос {} по пути {}'.format(request,path))
                if(find_in_hash(request) == "not find"):
                    responce = handler(request)
                else:
                    responce = find_in_hash(request)
                    print('найдено в кэше')
                add_hash([request,responce])
                add_log([then,request])
                now = time.time()
                delta = now - then
                print('Время обработки запроса {}'.format(delta))
                print('Ответ сервера:{}'.format(responce))
        return wrapper_level_2
        
    return the_wrapper_around_the_original_function
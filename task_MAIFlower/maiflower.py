import functools
import socket

# def logger(**options):
#     def decorator_inner(func: callable):
#         def wrapper(*args, **kwargs):
#             # print(args, kwargs, options)
#             # print("console" in options)
#             if(('console' in options) == True):
#                 # print("CONSOLE")
#                 print(func.__name__, *args, **kwargs)
#             if("file" in options == True):
#                 file = open("log.txt", 'a')
#                 file.write("".join(func.__name__, *args, **kwargs))
#                 file.close()
#             func(*args, **kwargs)
#         return wrapper
#     return decorator_inner

# def logger(func: callable):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         if('console' in kwargs):
#             print(func.__name__, *args)
#         if("file" in kwargs == True):
#             file = open("log.txt", 'a')
#             file.write("".join(func.__name__, *args, **kwargs))
#             file.close()
#         func(*args)
#     return wrapper

def logger(func: callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if("file" in args):
            file = open("log.txt", 'a')
            file.write("".join(func.__name__, *args, **kwargs))
            file.close()
        ret_val =  func(*args)
        print(ret_val, *args, **kwargs)
        return ret_val
    return wrapper

def cash(func: callable):
    @functools.wraps(func)
    def wrapper(cash_dict: dict, *args, **kwargs):
        # args_tuple = (*args)
        cash_dict[func.__name__] = {**kwargs, "args" : args}
        ret_val = func(cash_dict,*args, **kwargs)
        cash_dict[func.__name__]["return"] = ret_val
        return ret_val
    return wrapper    

class MaiFlower:
    """Maiflower is a fake server"""
    cash_dict = {}
    @logger
    def is_valid_ipv4_address(self, address):
        try:
            socket.inet_pton(socket.AF_INET, address)
        except AttributeError:  # no inet_pton here, sorry
            try:
                socket.inet_aton(address)
            except socket.error:
                return False
            return address.count('.') == 3
        except socket.error:  # not a valid address
            return False
        return True
    @logger
    def is_valid_port(self, port: int):
      if 1023 < port < 65536:
        return True
      return False

    def run_server(self, addr : str, port : int, *handlers, **kwargs):
        if(self.is_valid_ipv4_address(addr) and self.is_valid_port(port) ):
            for func in handlers:
                func[0](func[1])

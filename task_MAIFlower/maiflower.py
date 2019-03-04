import functools
import socket
import time

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
        # if("file" in args):
        #     file = open("log.txt", 'a')
        #     file.write("".join(func.__name__, *args, **kwargs))
        #     file.close()
        # func_name = func.__name__
        ret_val =  func(*args, **kwargs)
        print("Call: ",func.__name__)
        print("\targs: ", *args)
        print("\tkwargs: ", kwargs)
        print("\treturn: ", ret_val)
        return ret_val
    return wrapper

cash_dict = {}
def cash(ttl):
    """
    Cash decorator.
    Repeat args of function and return value in cash_dict.
    ttl - time to life, determines how long it takes
    to remove values from cash. one case - one unit of time.
    If ttl == 0 - it mean ttl = infinity
    """
    def decorator_inner(func):
        def wrapper( *args, **kwargs):
            in_out_dict = dict(ttl=ttl ,args=args, kwargs=kwargs)
            if len(cash_dict) != 0:
                for k in cash_dict:
                    if k == func.__name__:
                        if args == cash_dict[k]["args"] and kwargs == cash_dict[k]["kwargs"]:
                            return cash_dict[k]["ret_val"]
            ret_val = func(*args, **kwargs)
            in_out_dict.update({"ret_val":ret_val})
            cash_dict[func.__name__] =  in_out_dict

            # if cash_dict[k]["ttl"] == 0:
            temp_cash = cash_dict.copy()
            for k in temp_cash:
                if k != func.__name__:
                    if cash_dict[k]["ttl"] == 0:
                        del cash_dict[k]
                        continue
                    cash_dict[k]["ttl"] -=1
            return ret_val
        return wrapper
    return decorator_inner

def time_exec(func : callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.clock()
        ret_val = func(*args, **kwargs)
        distance_time = time.clock() - start_time
        print(f'Execution time {round(distance_time*1000000, 4)} usec')
        return ret_val
    return wrapper

def run_server( addr : str, port : int, cfg, *handlers):
        # if(self.is_valid_ipv4_address(addr) and self.is_valid_port(port) ):
        for func in handlers:
            if(len(func) == 3):
                func[0](*func[1], **func[2])
            else:
                func[0](*func[1])

# class MaiFlower:
#     """Maiflower is a fake server"""
#     cash_dict = {}
#     @logger
#     def is_valid_ipv4_address(self, address):
#         try:
#             socket.inet_pton(socket.AF_INET, address)
#         except AttributeError:  # no inet_pton here, sorry
#             try:
#                 socket.inet_aton(address)
#             except socket.error:
#                 return False
#             return address.count('.') == 3
#         except socket.error:  # not a valid address
#             return False
#         return True
#     @logger
#     def is_valid_port(self, port: int):
#       if 1023 < port < 65536:
#         return True
#       return False

#     def run_server(self, addr : str, port : int, *handlers, **kwargs):
#         if(self.is_valid_ipv4_address(addr) and self.is_valid_port(port) ):
#             for func in handlers:
#                 func[0](func[1])

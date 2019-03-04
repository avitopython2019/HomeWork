import maiflower
from maiflower import logger, cash, time_exec
# # @logger
# def say_hello(name):
#     print("Hello {}".format(name))

# # @logger
# @cash
# def make_json(cash_dict: dict, **kwargs):
#     return kwargs
@time_exec
@cash(2)
@logger
def sum(a, b):
    return a + b
@time_exec
@cash(2)
@logger
def mul(a, b):
    return a * b
@time_exec
@cash(2)
@logger
def sub(a, b):
    return a - b
@time_exec
@cash(2)
@logger
def div(a, b):
    return a / b


cfg = {"mul" : "/mul", "sum" : "/sum", "sub" : "/sub", "div" : "/div"}

maiflower.run_server("127.0.0.1", 8080, cfg, (sum, (4, 5)), (mul, (3, 2)), (div, (4,2)))
print(maiflower.cash_dict)
# json_val = make_json(my_server.cash_dict,  name="Miklail", university = "MAI")
mul(5,6)
print(maiflower.cash_dict)
# print(maiflower.cash_dict)

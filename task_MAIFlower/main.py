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
def sum(a, b, **kwargs):
    # print(*kwargs)
    return a + b
@time_exec
@cash(2)
@logger
def mul(a, b, **kwargs):
    # print(*kwargs)
    return a * b



# sum(4,5, name = "Misha")
# mul(5,4, name = "Anton")
# sum(4,5, name = "Nasty")
# # print(maiflower.cash_dict)

# sum(6,7, name = "John")
# print(maiflower.cash_dict)

# @cash(1)
# def func(a):
#     print(a)

# @cash(3)
# def bar(b):
#     print(b)

# func(5)

# print(maiflower.cash_dict)

# func(4)
# print(maiflower.cash_dict)

# func(3)
# print(maiflower.cash_dict)

# bar(7)
# print(maiflower.cash_dict)

# mul(5,6)
# print(maiflower.cash_dict)

# maiflower.func(1)
# print(maiflower.xyu_dict)
# maiflower.func(2)
# print (maiflower.xyu_dict)



# my_server = maiflower.MaiFlower()
maiflower.run_server("127.0.0.1", 8080, (sum, 4, 5, "Harry"))
# json_val = make_json(my_server.cash_dict,  name="Miklail", university = "MAI")
# print(my_server.cash_dict)

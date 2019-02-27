import maiflower
from maiflower import logger, cash
# @logger
def say_hello(name):
    print("Hello {}".format(name))

# @logger
@cash
def make_json(cash_dict: dict, **kwargs):
    return kwargs


my_server = maiflower.MaiFlower()
my_server.run_server("127.0.0.1", 8080, (say_hello,"Avito"))
json_val = make_json(my_server.cash_dict,  name="Miklail", university = "MAI")
print(my_server.cash_dict)
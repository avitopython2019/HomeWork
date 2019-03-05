import maiflower
from maiflower import logger, cash, time_exec

#Имитация базы данных студентов
student_db = dict(
    Misha =dict(
        id = 0,
        form="student",
        organization="MAI"),
    Anton = dict(
        id = 1,
        form="student",
        organization="MAI"),
    Andrew = dict(
        id = 2,
        form="student",
        organization="MAI"),
    John = dict(
        id = 3,
        form="student",
        organization="MIT",
        country="USA"))

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

@time_exec
@cash(2)
@logger
def get_student_data(name: str):
    # print(name)
    print (name, student_db[name])
    return student_db[name]

# print(student_db)


cfg = {"mul" :"/mul" , "sum" : "/sum", "sub" : "/sub", "div" : "/div"}

maiflower.run_server("127.0.0.1", 8080, cfg, (sum, (4, 5)), (mul, (3, 2)), (get_student_data, (),{"name":"Misha"}))
print(maiflower.cash_dict)
# json_val = make_json(my_server.cash_dict,  name="Miklail", university = "MAI")
# mul(5,6)
print(maiflower.cash_dict)
# print(maiflower.cash_dict)

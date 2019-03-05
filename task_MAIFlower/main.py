import maiflower
from maiflower import logger, cash, time_exec, valid

#Имитация базы данных студентов
student_db = dict(
    Misha =dict(
        id = 0,
        form="master",
        university="MAI"),
    Anton = dict(
        id = 1,
        form="master",
        university="MAI"),
    Andrew = dict(
        id = 2,
        form="bachelor",
        university="MAI"),
    John = dict(
        id = "sd",
        form="bachelor",
        university="MIT",
        country="USA"))

schema_student = {
    "type" : "object", 
    "properties": {
        "id" : {"type":"number"},
        "form" : {"type":"string"},
        "university" : {"type":"string"}
    }
}

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
@valid(schema_student)
def get_student(name: str):
    return student_db[name]


maiflower.run_server("http://example.com", 30001,
    (get_student, (),{"name":"Misha"}),
    (get_student, (),{"name":"John"}), # John - имеет неправильный id в бд, он не пройдёт валидацию
    )

print(f"Cash:\t {maiflower.cash_dict}\n") # cмотрим что лежит в кэш

maiflower.run_server("http://example.com", 30001,
    (sub, (4, 1), {}),
    (mul, (3, 2)), # Неправильный аргумент для передачи обработчика, см. docstring run_server
    (div, (6,2), {}),
    (sum, (5,4), {})
    )
print(f"Cash:\t {maiflower.cash_dict}\n") # cмотрим что лежит в кэш

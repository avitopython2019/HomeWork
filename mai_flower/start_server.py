import my_server as ms
handlers = ["addition","subtraction","division","multiplication","pow"]
num1 = 0
num2 = 0

ms.run_server("http://example.com", 30001, *handlers)
num1 = 10
num2 = 5
print()
handlers = ms.random_handlers(handlers)
ms.start_handlers(num1, num2, handlers)
#print(handlers)
print(ms.cache_dict)
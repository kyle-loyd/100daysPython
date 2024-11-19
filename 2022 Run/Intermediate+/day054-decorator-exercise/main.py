import time


def speed_calc_decorator(func):
    def wrapper():
        start = time.time()
        func()
        finish = time.time()
        print(f"{func.__name__} run speed: {finish - start}")
    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()

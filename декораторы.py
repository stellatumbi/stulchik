def log_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Функция '{func.__name__}' вызвана с аргументами: {args} {kwargs}")
        print(f"Вернуло: {result}")
        return result
    return wrapper

# Пример использования:
@log_decorator
def add(a, b):
    return a + b

add(2, 3)

import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция '{func.__name__}' выполнена за {end_time - start_time:.4f} секунд")
        return result
    return wrapper

# Пример использования:
@time_decorator
def multiply(a, b):
    time.sleep(1)  # Симуляция долгой работы
    return a * b

multiply(2, 3)

class Cache:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            print(f"Возвращаем кэшированный результат для {args}")
            return self.cache[args]
        result = self.func(*args)
        self.cache[args] = result
        return result

# Пример использования:
@Cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(10)

import time
from threading import Lock

class RateLimit:
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.calls = 0
        self.lock = Lock()
        self.start_time = time.time()

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with self.lock:
                current_time = time.time()
                if current_time - self.start_time > self.period:
                    self.calls = 0
                    self.start_time = current_time
                if self.calls < self.max_calls:
                    self.calls += 1
                    return func(*args, **kwargs)
                else:
                    print(f"Превышен лимит вызовов. Попробуйте позже.")
        return wrapper

# Пример использования:
@RateLimit(max_calls=2, period=5)
def greet(name):
    return f"Привет, {name}!"

print(greet('Alice'))
print(greet('Bob'))
print(greet('Charlie'))  # Этот вызов должен быть ограничен

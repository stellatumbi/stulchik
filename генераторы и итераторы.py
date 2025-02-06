def simple_prime_generator(limit):
    
    is_prime = [True] * limit


    if limit > 0:
        is_prime[0] = False
    if limit > 1:
         is_prime[1] = False

    
    for number in range(2, limit):
        
        if is_prime[number]:
            yield number

            
            for multiple in range(number + number, limit, number):
                is_prime[multiple] = False


# Пример использования
for prime in simple_prime_generator(15):
    print(prime) 


class SimpleCyclicIterator:


    def __init__(self, items):
       
        
        self.items = items # Список для перебора
        self.index = 0 # Начальный индекс
        self.length = len(items) # Длина списка

    def __iter__(self):
       
        return self

    def __next__(self):
        
        current = self.items[self.index]  # Берем текущий элемент
        self.index = (self.index + 1) % self.length # Обновляем индекс (делаем круг)
        return current # Возвращаем элемент


# Пример использования
it = SimpleCyclicIterator([1, 2, 3])
for _ in range(7):
    print(next(it))
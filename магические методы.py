class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        """
        Возвращает строковое представление объекта.
        """
        return f"Person: {self.name}, Age: {self.age}"

# Пример использования
p = Person("Alice", 25)
print(p)  # "Person: Alice, Age: 25"








class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        """
        Возвращает строковое представление объекта.
        """
        return f"Person: {self.name}, Age: {self.age}"

    def __eq__(self, other):
        """
        Проверяет равенство объектов.
        """
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        """
        Сравнивает объекты по возрасту. Младше.
        """
        return self.age < other.age

    def __gt__(self, other):
        """
        Сравнивает объекты по возрасту. Старше.
        """
        return self.age > other.age

# Пример использования
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)
p3 = Person("Alice", 25)

print(p1 == p3)  # True
print(p1 == p2)  # False
print(p1 < p2)   # True
print(p1 > p2)   # False
print(p2 > p1)   # True








class Collection:
    def __init__(self, people: list):
        self.people = people

    def __add__(self, person):
        """
        Добавляет нового человека в коллекцию.
        """
        self.people.append(person)
        return self

    def __len__(self):
        """
        Возвращает количество людей в коллекции.
        """
        return len(self.people)

# Пример использования
c = Collection([Person("Alice", 25), Person("Bob", 30)])
print(len(c))  # 2

c = c + Person("Charlie", 22)
print(len(c))  # 3










class Collection:
    def __init__(self, people: list):
        self.people = people

    def __add__(self, person):
        """
        Добавляет нового человека в коллекцию.
        """
        self.people.append(person)
        return self

    def __len__(self):
        """
        Возвращает количество людей в коллекции.
        """
        return len(self.people)

# Пример использования
c = Collection([Person("Alice", 25), Person("Bob", 30)])
print(len(c))  # 2

c = c + Person("Charlie", 22)
print(len(c))  # 3





class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}"

class Collection:
    def __init__(self, people: list):
        self.people = people

    def __add__(self, person):
        """
        Добавляет нового человека в коллекцию.
        """
        self.people.append(person)
        return self

    def __len__(self):
        """
        Возвращает количество людей в коллекции.
        """
        return len(self.people)

    def __getitem__(self, index):
        """
        Возвращает человека по индексу.
        """
        return self.people[index]

# Пример использования
c = Collection([Person("Alice", 25), Person("Bob", 30)])
print(c[0])  # "Person: Alice, Age: 25"







class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}"

class Collection:
    def __init__(self, people: list):
        self.people = people

    def __add__(self, person):
        """
        Добавляет нового человека в коллекцию.
        """
        self.people.append(person)
        return self

    def __len__(self):
        """
        Возвращает количество людей в коллекции.
        """
        return len(self.people)

    def __getitem__(self, index):
        """
        Возвращает человека по индексу.
        """
        return self.people[index]

    def __call__(self):
        """
        Возвращает список всех имен людей в коллекции.
        """
        return [person.name for person in self.people]

# Пример использования
c = Collection([Person("Alice", 25), Person("Bob", 30)])
print(c())  # ["Alice", "Bob"]



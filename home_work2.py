# 1
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Транспортное средство заводится.")

    def stop(self):
        print("Транспортное средство останавливается.")

    def info(self):
        return f"Марка: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.year}"

# 2
class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def start(self):
        print("Машина заводится.")

    def stop(self):
        print("Машина останавливается.")

    def open_trunk(self):
        print("Багажник открыт.")

    def info(self):
        base_info = super().info()
        return f"{base_info}\nКоличество дверей: {self.doors}\nТип: Машина"


class Bicycle(Vehicle):
    def __init__(self, brand, model, year, type_of_bicycle):
        super().__init__(brand, model, year)
        self.type_of_bicycle = type_of_bicycle

    def start(self):
        print("Велосипед начинает движение.")

    def stop(self):
        print("Велосипед останавливается.")

    def ring_bell(self):
        print("Звонок звенит.")

    def info(self):
        base_info = super().info()
        return f"{base_info}\nТип велосипеда: {self.type_of_bicycle}\nТип: Велосипед"


class Boat(Vehicle):
    def __init__(self, brand, model, year, length):
        super().__init__(brand, model, year)
        self.length = length

    def start(self):
        print("Лодка отплывает.")

    def stop(self):
        print("Лодка приплывает.")

    def anchor(self):
        print("Якорь спущен.")

    def info(self):
        base_info = super().info()
        return f"{base_info}\nДлина лодки: {self.length} метров\nТип: Лодка"


car = Car("Ford", "Mustang", 2022, 2)
bicycle = Bicycle("Cannondale", "Trail 7", 2023, "горный")
boat = Boat("Sea Ray", "SPX 190", 2021, 6.0)


print("Информация о транспортном средстве:")
print(car.info())
print("-" * 30)
car.start()
car.open_trunk()
car.stop()

print("\nИнформация о транспортном средстве:")
print(bicycle.info())
print("-" * 30)
bicycle.start()
bicycle.ring_bell()
bicycle.stop()

print("\nИнформация о транспортном средстве:")
print(boat.info())
print("-" * 30)
boat.start()
boat.anchor()
boat.stop()


# задание которые давали на уроке 
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} ест")

    def sleep(self):
        print(f"{self.name} спит")


class Walker:
    def walk(self):
        print(f"{self.name} ходит")


class Swimmer:
    def swim(self):
        print(f"{self.name} плавает")


class Flyer:
    def fly(self):
        print(f"{self.name} летает")


class Penguin(Animal, Walker, Swimmer):
    def __init__(self, name):
        super().__init__(name)

    def describe(self):
        print(f"{self.name} может ходить и плавать.")


class Duck(Animal, Walker, Swimmer, Flyer):
    def __init__(self, name):
        super().__init__(name)

    def describe(self):
        print(f"{self.name} может ходить, плавать и летать.")


class Bat(Animal, Flyer):
    def __init__(self, name):
        super().__init__(name)

    def describe(self):
        print(f"{self.name} может летать.")


penguin = Penguin("Пингвин Пётр")
penguin.describe()
penguin.walk()
penguin.swim()
penguin.eat()
penguin.sleep()

print("-" * 30)

duck = Duck("Утка Даша")
duck.describe()
duck.walk()
duck.swim()
duck.fly()
duck.eat()
duck.sleep()

print("-" * 30)

bat = Bat("Летучая мышь Бэт")
bat.describe()
bat.fly()
bat.eat()
bat.sleep()

# from abc import ABC, abstractmethod
# # 1
# class Animal(ABC):
#     def __init__(self, name: str, age: int):
#         self.name = name 
#         self.age = age 
    
#     @property
#     @abstractmethod
#     def make_sound(self):
#         pass
    
    
#     @abstractmethod
#     def display_info(self):
#         pass
# # 2  
# class Lion(Animal):
    
#     @property
#     def make_sound(self):
#         return 'Рррр'
    
#     def display_info(self):
#         return (
#             f"🐾 Информация о Льве:\n"
#             f"  Имя: {self.name}\n"
#             f"  Ему исполнилось: {self.age} лет\n"
#             f"  Он умеет рычать: {self.make_sound}\n"
#         )
# class Elephant(Animal):
    
#     @property
#     def make_sound(self):
#         return 'Уууу'
    
#     def display_info(self):
#         return (
#             f"🐘 Информация о Слоне:\n"
#             f"  Имя: {self.name}\n"
#             f"  Ему исполнится: {self.age} лет\n"
#             f"  Он умеет издавать звук: {self.make_sound}\n"
#         )
# # 3
# def introduce_animal(animal: Animal):
#     print(animal.display_info())
#     print(f"🔊 Звук: {animal.make_sound}")
#     print('-' * 30)


# lion = Lion(name='Симба', age=11)
# elephant = Elephant(name='Джамбо', age=50)
   
# result = [lion, elephant]

# for res in result:  
#     introduce_animal(res)
    
    
# Задание которое давали на уроке 

class Employee:
    def __init__(self, name: str, base_rate: float):
        self.name = name
        self.base_rate = base_rate
        

    def calculate_salary(self):
        return 0.0

    def display_info(self):
        return (
            f"Имя сотрудника: {self.name}\n"
            f"Базовая ставка: {self.base_rate}\n"
            f"Зарплата: {self.calculate_salary()}\n"
        )
        
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return self.base_rate * 1.5

class PartTimeEmployee(Employee):
    def __init__(self, name: str, base_rate: float, hours_worked: float):
        super().__init__(name, base_rate)
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.base_rate * 0.5 * self.hours_worked

def process_salary(employee: Employee):
    print(employee.display_info())


full_time_employee = FullTimeEmployee(name='Рустам', base_rate=2000)
part_time_employee = PartTimeEmployee(name='Алексей', base_rate=1000, hours_worked=8)

result = [full_time_employee, part_time_employee]

for res in result:
    process_salary(res)

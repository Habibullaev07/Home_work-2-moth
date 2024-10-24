# 1
class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
# 2
    def __make_computations(self):
        print(f"{'-' * 40} \nAрифмитические действии:")
        print(f"Сложение - {self.__cpu + self.__memory} \nВычитание - {self.__cpu - self.__memory} \nУмножение - {self.__cpu * self.__memory}")
        print(f"Деление - {self.__cpu / self.__memory}" if self.__memory != 0 else print("Невозможно разделить на ноль"))
        
# 3
    def perform_computations(self):
        self.__make_computations()
    
    @property
    def cpu(self):
        return self.__cpu
    
     
    @property
    def memory(self):
        return self.__memory
    
# информация
    def __info(self):
    
        print(f"Информация Ноутбука: \nПроцессор - {self.cpu} ядра \nПамять - {self.memory}-гб")
    
    def information(self):
        return self.__info()

# 4
class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card
# 5
    @property
    def memory_card(self):
        return self.__memory_card
    
# 6
    def info(self):
        super().information()
        print(f"Карта памяти - {self.memory_card}")
    
# Пользователь
cpu = float(input("Введите значение процессора: "))
memory = float(input("Введите значение памяти: "))
memory_card = float(input("Введите значение карты памяти: "))

# Вывод на экран
print()
computer = Computer(cpu, memory)
computer.information()
computer.perform_computations()
print('-' * 40)
laptop = Laptop(cpu, memory, memory_card)
laptop.info()
laptop.perform_computations()
    



    
    

# 1
# class Fruits:
#     def __init__(self, name, color, weight):
#         self.name = name
#         self.color = color 
#         self.weight = weight
        
#     def info(self):
#         print("Информация о нашего нового фрукта".center(100))
#         print(f"Имя фрукта - {self.name}\nЦвет нашего фрукта - {self.color}\nВес нашего фрукта - {self.weight}")
#         print("Все вы получили информацию про - Джекфрут\n")
#         url = "https://ru.wikipedia.org/wiki/Джекфрут"
#         print(f"Если хотите получить полную информацию:\nПерейдите на этот сайт: {url}")

       
# info_name_fruct = 'Это самый редкий вид фрукта: Он состаит из древесное растение вид рода Артокарпус семейства Тутовые'
# fruits = Fruits(f'Джекфрут\n{info_name_fruct}\n', 'светло-зеленый', '8-11кг')
# fruits.info()

# 2
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def check_pages(self, user):
        access_site_1 = "Первый этап".center(70)
        access_site = "Если хотите разблакировать ссылку на сайт и прочитать:\nТогда пройдите арифматическую действия"
        
        if user < 100:
            print(f"Вы выбрали менее сто страниц, точнее {user}, страницу\n")
            print(access_site_1)
            print(access_site)
        
        elif user > 100 and user <= 300:
            print(f"Вы выбрали в радиусе 100-300 страниц, точнее {user}, страницу\n")
            print(access_site_1)
            print(access_site)

        else:
            print(f"Вы выбрали больше 300 страниц,  точнее {user}, cтраницу\n")
            print(access_site_1)
            print(access_site)
        self.matematic()
    
    def check_sait(self, write_user):

        if write_user == 0:
            print(f"Вот сайт - https://mybook.ru/author/napoleon-hill/dumaj-i-bogatej-1/read/\nНа книгу Думай и богатей")
        elif write_user == 1:
            exit
        else:
            print("Доступ заблокирован")
                
    def result_book(self):
        print("Наполеон Хилл: ДУМАЙ И БОГАТЕЙ".center(70))
        print(f"Имя книги - {self.title}\nАвтор книге - {self.author}\nСтраниц в книге: {self.pages}")
        
    def matematic(self):
        import random
        num_1 = (random.randint(0, 100))
        num_2 = random.randint(0, 100)
        print(f"Сколько будет: {num_1} + {num_2}")
        f = "Напишите ответ"
        user = int(input(f"{f} {num_1} + {num_2} = "))
        
        if user == num_1 + num_2:
            print("Вы прошли")
            print("Второй этап".center(70))
            print("Если хотите разблакировать ссылку на сайт и прочитать: Ведите 0\nЕсли хотите выйти 1")
            self.check_sait
            
        else:
            print("Вы не прошли арифметическую действия:\nДоступ заблакирован")
            exit()
            
  

book = Book("Думай и богатей", "Наполеон Хилл", 384)
book.result_book()
book.check_pages(int(input("Выберите страницу каторую хотите посетить: ")))
book.check_sait(int(input(": ")))
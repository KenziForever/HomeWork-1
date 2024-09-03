# принципы ооп
# 4 Наследование,Полиморфизм,Инкапсуляция,Абстракция
# gitignore
# на основе одного класса можно создать другие классы

from lesson1 import Manga
# naruto=Manga('Naruto','Kishimoto')

# print(naruto)

# cупер класс\родительский класс
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def reads(self):
        print('я читаю книгу:',self.title)

    def words_author(self):
        print('привет меня зовут:',self.author,' читай с лево на право')

# DRY -
book1 = Book('властелин колец','Толкин')
book1.reads()
book1.words_author()


class Manga(Book):
    def __init__(self, title, author,png='png'):
        super().__init__(title, author)
        Book.__init__(self, title, author)
        self.png = png
    def reads(self):
        print('я читаю мангу:',self.title)
        super().words_author()



manga=Manga('naruto','Kishimoto')
manga.reads()
# ООП - обьектно ориентированное программирование

p = '1', 1, 1.2, [], {}, (), False, None
print(type(p))


# def a(b):
#     print(b)

class Manga:
    color = 'WB'

    # метод
    def read(self):
        print('читаю мангу', self.name)

    def __init__(self, name, avtore):
        self.name = name
        self.avtore = avtore

    def __str__(self):
        return f'название: {self.name}\n' \
               f'автор: {self.avtore}\n'

# экземпляр класса обьект класса
chillpill = Manga('чиллпил', 'бека')
JJG = Manga('маг битва', 'геге окутами')
# read(chillpill)
# JJG.read()
# chillpill.read()
# print(JJG)
# print(chillpill)
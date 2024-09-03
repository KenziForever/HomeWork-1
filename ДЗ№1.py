
class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f'Nickname: {self.nickname}, Superpower: {self.superpower}, Health Points: {self.health_points}'

    def catchphrase_length(self):
        return len(self.catchphrase)

    def __repr__(self):
        return f'Catchphrase: {self.catchphrase}'


if __name__ == '__main__':
    hero = SuperHero(name='Clark Kent', nickname='Superman', superpower='Flight', health_points=100,
                     catchphrase='Truth, Justice, and the American Way!')

    print('Hero\'s Name:', hero.get_name())

    hero.double_health()
    print('Hero\'s Health Points after doubling:', hero.health_points)

    print(hero)

    print(hero.__repr__())

    print('Catchphrase Length:', hero.catchphrase_length())

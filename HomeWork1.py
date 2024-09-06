
class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.flying = False,
        self.damage = 32

    def get_name(self):
        return self.name

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health Points: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)

    def speak(self):
        return self.catchphrase

hero = SuperHero(
    name='Clark Kent',
    nickname='Superman',
    superpower='Flight and Super Strength',
    health_points=100,
    catchphrase='I am the greatest hero of all time!'
)

print(hero.get_name())
hero.double_health()
print(hero)
print(len(hero))
print(hero.speak())

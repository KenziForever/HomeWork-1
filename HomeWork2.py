from HomeWork1 import SuperHero
class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, wing_span):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.wing_span = wing_span

    def double_health(self):
        super().double_health()
        print(f"{self.nickname} is soaring with a wingspan of {self.wing_span}!")

    def __str__(self):
        return super().__str__() + f", Wing Span: {self.wing_span}"

class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, terrain_mastery):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.terrain_mastery = terrain_mastery

    def double_health(self):
        super().double_health()
        print(f"{self.nickname} has mastery over {self.terrain_mastery}!")

    def __str__(self):
        return super().__str__() + f", Terrain Mastery: {self.terrain_mastery}"

class Villain(SuperHero):
    people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, evil_power):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.evil_power = evil_power

    def gen_x(self):
        pass

    def crit(self):
        self.damage **= 2
        print(f"{self.nickname}'s damage is now {self.damage}!")

    def __str__(self):
        return super().__str__() + f", Evil Power: {self.evil_power}, People: {self.people}"

air_hero = AirHero(name='John Doe', nickname='SkyMaster', superpower='Flight', health_points=100, catchphrase='To the skies!', wing_span=20)
earth_hero = EarthHero(name='Jane Doe', nickname='RockQueen', superpower='Earth Control', health_points=150, catchphrase='Earth is my domain!', terrain_mastery='mountains')
villain = Villain(name='Lex Luthor', nickname='The Lethal', superpower='Genius Intellect', health_points=200, catchphrase='I will rule the world!', evil_power='Dark Magic')

print(air_hero.get_name())
air_hero.double_health()
print(air_hero)
print(len(air_hero))
print(air_hero.speak())

print(earth_hero.get_name())
earth_hero.double_health()
print(earth_hero)
print(len(earth_hero))
print(earth_hero.speak())

villain.crit()
print(villain)

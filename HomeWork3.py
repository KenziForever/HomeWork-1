class Flying:
    def __init__(self):
        self.state = "на земле"

    def fly(self):
        self.state = "в воздухе"
        print(f"Амфибия сейчас {self.state}.")

class Swimming:
    def __init__(self):
        self.state = "на земле"

    def swim(self):
        self.state = "в воде"
        print(f"Амфибия сейчас {self.state}.")

class Amphibian(Flying, Swimming):
    def __init__(self):
        Flying.__init__(self)
        Swimming.__init__(self)
        self.state = 'на земле'
        print(f'Амфибия сейчас {self.state}.')

    def land(self):
        self.state = "на земле"
        print(f"Амфибия сейчас {self.state}.")


amphibian = Amphibian()


amphibian.fly()
amphibian.swim()
amphibian.land()

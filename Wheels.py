class Wheels():
    def __init__(self):
        '''
        Robots have arms, wheels, and a body by default. Sensors or add-ons can be appended later and are visible for attack
        '''
        self.health = 100
        self.armor = 100
        self.movement = 50
        self.accuracy = 50
        self.dodge = 50


    def equip(self):
        pass

    def use(self):
        pass

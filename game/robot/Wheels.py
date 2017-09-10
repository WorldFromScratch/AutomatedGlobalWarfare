import uuid

class Wheels():
    def __init__(self):
        '''
        Robots have wheels and a body by default. Sensors or add-ons can be appended later and are visible for attack
        '''
        self.health = 100
        self.armor = 100
        self.movement = 50
        self.accuracy = 50
        self.dodge = 50

        self.startingHealth = 100
        self.startingArmor = 100
        self.id = uuid.uuid4().hex

    def getId(self):
        return self.id

    def toDict(self):
        return {'id':self.id,'health':self.health,'armor':self.armor,'movement':self.movement,'dodge':self.dodge}

    def reset(self):
        self.health = self.startingHealth
        self.armor = self.startingArmor

    def equip(self):
        pass

    def use(self):
        pass

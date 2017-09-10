import uuid

class Body():
    def __init__(self):
        '''
        Robots have arms, wheels, and a body by default. Sensors or add-ons can be appended later and are visible for attack
        '''
        self.health = 100
        self.armor = 700
        self.dodge = 50

        self.startingHealth = 100
        self.startingArmor = 700
        self.id = uuid.uuid4().hex

    def getId(self):
        return self.id

    def toDict(self):
        return {'id':self.id,'health':self.health,'armor':self.armor,'dodge':self.dodge}

    def reset(self):
        self.health = self.startingHealth
        self.armor = self.startingArmor

    def equip(self):
        pass

    def use(self):
        pass

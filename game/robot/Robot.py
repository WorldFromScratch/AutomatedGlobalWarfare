from Arm import Arm
from Wheels import Wheels
from Body import Body
from importlib import import_module

class Robot():

    def __init__(self, battle, stratName):
        '''
        Robots have arms, wheels, and a body by default. Sensors or add-ons can be appended later and are visible for attack
        '''
        self.leftArm = Arm()
        self.rightArm = Arm()
        self.body = Body()
        self.wheels = Wheels()
        self.addOns = []
        self.stratName = stratName
        self.battle = battle
        p, m = 'robot.' + self.stratName, 'strat'

        mod = import_module(p)
        self.strategy = getattr(mod, m)

    def use(self, part):

        part.use()

    def wait(self):
        pass

    def getUsedOn(self,part):
        pass

    def getFunctioningParts(self):
        #always available
        parts = [self.leftArm,self.rightArm,self.body,self.wheels]

        parts.extend(self.addOns)

        functioningParts = []
        for part in parts:
            if part.health > 0:
                functioningParts.append(part)

        return functioningParts

    def status(self):
        if self.body.health > 0:
            return "Alive"
        else:
            return "Dead"


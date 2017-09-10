from Wheels import Wheels
from Body import Body
from importlib import import_module
from AddOn import Arm
import uuid


class Robot():

    def __init__(self, battle, stratName):
        '''
        Robots have arms, wheels, and a body by default. Sensors or add-ons can be appended later and are visible for attack
        '''

        self.body = Body()
        self.wheels = Wheels()
        self.addOns = [Arm(),Arm()]
        self.stratName = stratName
        self.battle = battle
        p, m = 'robot.' + self.stratName, 'strat'

        mod = import_module(p)
        self.strategy = getattr(mod, m)
        self.id = uuid.uuid4().hex

    def toDict(self):
        infoDict = {'id':self.id,'status':self.status(),'body':self.body.toDict(),'wheels':self.wheels.toDict()}

        addOnInfo = []
        for addOn in self.addOns:
            addOnInfo.append(addOn.toDict())
        infoDict['addOns':addOnInfo]

        return infoDict

    def getId(self):
        return self.id

    def reset(self):
        self.body.reset()
        self.wheels.reset()
        for addOn in self.addOns:
            addOn.reset()

    def use(self, part):

        part.use()

    def wait(self):
        pass

    def getUsedOn(self,part):
        pass

    def getFunctioningParts(self):
        #always available
        parts = [self.body,self.wheels]

        parts.extend(self.addOns)

        functioningParts = []
        for part in parts:
            if part.health > 0:
                functioningParts.append(part)

        return functioningParts

    def getFunctioningPartIds(self):
        #always available
        parts = {'body':self.body.id}
        if self.wheels.health > 0:
            parts['wheels'] = self.wheels.id

        functioningAddOns = []
        for addOn in self.addOns:
            if addOn.health > 0:
                functioningAddOns.append(addOn.id)
        parts['addOns'] = functioningAddOns
        return parts

    def status(self):
        if self.body.health > 0:
            return "Alive"
        else:
            return "Dead"


from Arm import Arm
from Wheels import Wheels
from Body import Body
import random

class Robot():

    def __init__(self, battle, stratNum = 0):
        '''
        Robots have arms, wheels, and a body by default. Sensors or add-ons can be appended later and are visible for attack
        '''
        self.leftArm = Arm()
        self.rightArm = Arm()
        self.body = Body()
        self.wheels = Wheels()
        self.addOns = []
        self.stratNum = stratNum
        self.battle = battle

    def strategy(self,robot):

        if self.stratNum == 0:
            if self.rightArm.health > 0:
                self.battle.usePartOnPart(self.rightArm,robot.body)
            elif self.leftArm.health > 0:
                self.battle.usePartOnPart(self.leftArm, robot.body)
        else:
            parts = robot.getFunctioningParts()
            if len(parts) == 1:
                attackPart = parts[0]
            else:
                attackPart = parts[random.randint(0,len(parts)-1)]
            if self.rightArm.health > 0:
                self.battle.usePartOnPart(self.rightArm,attackPart)
            elif self.leftArm.health > 0:
                self.battle.usePartOnPart(self.leftArm, attackPart)

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

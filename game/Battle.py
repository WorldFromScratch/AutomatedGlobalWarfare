from robot.Robot import Robot
import random
from importlib import import_module

class Battle():

    def __init__(self, robot1Strat, robot2Strat):
        self.robot1 = Robot(self, robot1Strat)
        self.robot2 = Robot(self, robot2Strat)
        self.partsDict = {}

        for robot in [self.robot1,self.robot2]:
            self.partsDict[robot.body.id] = robot.body
            self.partsDict[robot.wheels.id] = robot.wheels
            for addOn in robot.addOns:
                self.partsDict[addOn.id] = addOn

    def toDict(self):
        return {'robots':[self.robot1.toDict(),self.robot2.toDict()]}

    def autoBattle(self):
        battleResults = []
        for i in range(1000):
            self.robot1.reset()
            self.robot2.reset()
            if i % 2 == 0:
                while self.robot1.status() != "Dead" and self.robot2.status() != "Dead":
                    self.robot1.strategy(self.robot2,self.robot1)
                    if self.robot2.status() != "Dead":
                        self.robot2.strategy(self.robot1,self.robot2)
                    else:
                        break
            else:
                while self.robot1.status() != "Dead" and self.robot2.status() != "Dead":
                    self.robot2.strategy(self.robot1,self.robot2)
                    if self.robot1.status() != "Dead":
                        self.robot1.strategy(self.robot2,self.robot1)
                    else:
                        break
            battleResults.append([self.robot1.status(), self.robot2.status()])
        count = [0,0]
        for result in battleResults:
            if result[0] == 'Alive':
                count[0] += 1
            else:
                count[1] += 1

        return count

    def callFunctionFromDict(self, commandDict):
        if commandDict['function'] == 'usePartOnPart':
            self.usePartOnPart(self.getPartFromId(commandDict['usePart']),self.getPartFromId(commandDict['usedOnPart']))

    def getPartFromId(self,id):
        return self.partsDict[id]

    def usePartOnPart(self, usePart, usedOnPart):
        info = {}
        info['command'] = {'usePart':usePart.getId(),'usedOnPart':usedOnPart.getId(),'function':'usePartOnPart'}
        if usePart.use() == "Attack":
            attackChance = float(usePart.attack) / (usePart.attack + usedOnPart.dodge)
            if random.uniform(0, 1) < attackChance:
                info['result'] = {'success':True}
                #attack succeeds
                if usedOnPart.armor > 0:
                    if usedOnPart.armor > usePart.attack:
                        info['result']['effect'] = {'partId': usedOnPart.getId(), 'function': usePart.use(),
                                                    'effectedAttributes': [['Armor', -usePart.attack]]}
                        usedOnPart.armor -= usePart.attack

                    else:
                        info['result']['effect'] = {'partId': usedOnPart.getId(), 'function': usePart.use(),
                                                    'effectedAttributes': [['Armor', usedOnPart.armor],
                                                    ['Health', (usePart.attack - usedOnPart.armor)]]}
                        usedOnPart.health -= (usePart.attack - usedOnPart.armor)
                        usedOnPart.armor = 0

                else:
                    usedOnPart.health -= usePart.attack
                    info['result']['effect'] = {'partId': usedOnPart.getId(), 'function': usePart.use(),
                                                'effectedAttributes': [['Health', -usePart.attack]]}
            else:
                info['result'] = {'success': False}
        return info

battle = Battle('test','test2')
print battle.autoBattle()

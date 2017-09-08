from Robot import Robot
import random

class Battle():

    def __init__(self):
        self.robot1 = Robot(self,1)
        self.robot2 = Robot(self)

    def autoBattle(self):
        battleResults = []
        for i in range(1000):
            self.robot1 = Robot(self, 1)
            self.robot2 = Robot(self)
            if i % 2 == 0:
                while self.robot1.status() != "Dead" and self.robot2.status() != "Dead":
                    self.robot1.strategy(self.robot2)
                    if self.robot2.status() != "Dead":
                        self.robot2.strategy(self.robot1)
                    else:
                        break
            else:
                while self.robot1.status() != "Dead" and self.robot2.status() != "Dead":
                    self.robot2.strategy(self.robot1)
                    if self.robot1.status() != "Dead":
                        self.robot1.strategy(self.robot2)
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

    def usePartOnPart(self, usePart, usedOnPart):

        if usePart.use() == "Attack":
            attackChance = float(usePart.attack) / (usePart.attack + usedOnPart.dodge)
            if random.uniform(0, 1) < attackChance:
                #attack succeeds
                if usedOnPart.armor > 0:
                    if usedOnPart.armor > usePart.attack:
                        usedOnPart.armor -= usePart.attack
                    else:
                        usedOnPart.health -= (usePart.attack - usedOnPart.armor)
                        usedOnPart.armor = 0
                else:
                    usedOnPart.health -= usePart.attack

battle = Battle()
print battle.autoBattle()

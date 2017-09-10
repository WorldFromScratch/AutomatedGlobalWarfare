import random

def strat(robot,opposingRobot):
    parts = opposingRobot.getFunctioningParts()

    if len(parts) == 1:
        attackPart = parts[0]
    else:
        attackPart = parts[random.randint(0, len(parts) - 1)]

    for addOn in robot.addOns:
        if addOn.health > 0:
            robot.battle.usePartOnPart(addOn, attackPart)

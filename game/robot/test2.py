import random

def strat(robot,opposingPartIds):
    parts = opposingPartIds.keys()

    if len(parts) == 1:
        attackPart = parts[0]
    else:
        attackPart = parts[random.randint(0, len(parts) - 1)]

    for addOn in robot.addOns:
        if addOn.health > 0:
            robot.battle.usePartOnPart(addOn, attackPart)

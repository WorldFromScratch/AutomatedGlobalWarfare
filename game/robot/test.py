
def strat(robot,opposingRobot):
    for addOn in robot.addOns:
        if addOn.health > 0:
            return robot.battle.usePartOnPart(addOn, opposingRobot.body)


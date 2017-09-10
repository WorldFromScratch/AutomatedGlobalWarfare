import random

def strat(robot,opposingRobot):
    parts = opposingRobot.getFunctioningParts()

    if len(parts) == 1:
        attackPart = parts[0]
    else:
        attackPart = parts[random.randint(0, len(parts) - 1)]
    if robot.rightArm.health > 0:
        robot.battle.usePartOnPart(robot.rightArm, attackPart)
    elif robot.leftArm.health > 0:
        robot.battle.usePartOnPart(robot.leftArm, attackPart)
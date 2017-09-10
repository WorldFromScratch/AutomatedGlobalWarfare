
def strat(robot,opposingRobot):
    if robot.rightArm.health > 0:
        robot.battle.usePartOnPart(robot.rightArm, opposingRobot.body)
    elif robot.leftArm.health > 0:
        robot.battle.usePartOnPart(robot.leftArm, opposingRobot.body)

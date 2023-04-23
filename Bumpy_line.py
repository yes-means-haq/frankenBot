from gpiozero import CamJamKitRobot
import time

# Create a robot object
robot = CamJamKitRobot()

def slowRight():
    robot.value = (-0.5, 0)
    time.sleep(0.2)
def slowLeft():
    robot.value = (0.5, -0.5)
    time.sleep(0.2)

def slowForward():
    robot.value = (-0.6, -0.6)
    time.sleep(0.05)

def slowBackward():
    robot.value = (0.6, 0.6)
    time.sleep(0.05)

def stop():
    robot.value = (0, 0)

def searchLine():
    slowRight()
    slowLeft()
    slowLeft()
    slowRight()
    slowForward()
    time.sleep(0.5)

    return 0



for i in range(5):
    searchLine()



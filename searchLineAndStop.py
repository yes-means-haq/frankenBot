import time
from gpiozero import CamJamKitRobot, LineSensor
import random

# Create a robot object
robot = CamJamKitRobot()

# Set variables for the GPIO pins
pinLineFollower = 25

# Create a LineSensor object
sensor = LineSensor(pinLineFollower)

# Define the functions that will be called when the line is
# detected or not detected
def lineseen():
    print("Line seen")
    robot.stop()
    exit(0)

def linenotseen():
    print("No line seen")


# Tell the program what to do with a line is seen
sensor.when_line = lineseen
# And when no line is seen
sensor.when_no_line = linenotseen


def slowRight():
    robot.value = (-0.5, 0)
    time.sleep(0.4)

def slowLeft():
    robot.value = (0, -0.5)
    time.sleep(0.4)

def slowForward():
    robot.value = (-0.6, -0.6)
    time.sleep(0.025)

def slowBackward():
    robot.value = (0.6, 0.6)
    time.sleep(0.025)

def searchLine():
    direction = random.choice([1, 2])
    if direction == 1:
        # Move right and left
        slowRight()
        slowLeft()
        slowLeft()
        slowRight()
    else:
        # Move forward and backward
        slowForward()
        slowBackward()

try:
    # Repeat the next indented block forever
    while True:
        searchLine()
        time.sleep(0.5)

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    print("Exiting")

from gpiozero import CamJamKitRobot
from sshkeyboard import listen_keyboard
import sys

robot = CamJamKitRobot()

def on_press(key):
    print(key)
    if key == 'up':
        robot.forward()
    elif key == 'down':
        robot.backward()
    elif key == 'left':
        robot.left()
    elif key == 'right':
        robot.right()
    elif key == 'q':
        exit()

def on_release(key):
    robot.stop()







listen_keyboard(on_press=on_press, on_release=on_release)
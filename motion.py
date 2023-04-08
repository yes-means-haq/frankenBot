from gpiozero import CamJamKitRobot
from sshkeyboard import listen_keyboard

robot = CamJamKitRobot()

def on_press(key):
    if key == 'up':
        robot.forward()
    elif key == 'down':
        robot.backward()
    elif key == 'left':
        robot.left()
    elif key == 'right':
        robot.right()

def on_release(key):
    robot.stop()

listen_keyboard(on_press=on_press, on_release=on_release)

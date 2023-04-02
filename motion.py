import time
import curses
import readchar
from gpiozero import CamJamKitRobot

# Pour executer : cd ~/Documents/frankenbot && sudo python3 motion.py

robot = CamJamKitRobot()

# Initialize the curses library
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(True)

def cleanupCurses():
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()



try:
    while True:
        # Read a single character from the console input
        char = stdscr.getch()
        char = chr(char)
        print(char)
        print("\n")

        if char == 'Ă':
            robot.forward()
        elif char == 'ă':
            robot.backward(1)
        elif char == 'Ą':
            robot.left(0.3)
        elif char == 'ą':
            robot.right(0.3)
        elif char == 's':
            robot.stop()
        elif char == 'q':
                break
        else:
            robot.stop()

    robot.stop() # stop bot before leave

    # Clean up the curses library
    cleanupCurses()

except KeyboardInterrupt:
    robot.stop()
    print("\nKill program")

    # Clean up the curses library
    cleanupCurses()


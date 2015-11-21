'''
The series of python files `playing_with_curses_tuto*.py` follow a tutorial
on the python module `curses` which should allow us to obtain a colored
visualization for the chess game.

This first file correspond to the youtube tutorial on the following website:
https://www.youtube.com/watch?v=yxIC15GVv6w
'''

# import the module and create a screen object
import curses
screen = curses.initscr()

# Define a message to be displayed
message = "Let's play some chess!"

# Add the message to screen object
screen.addstr(0, 0, message)
'''
    The first two arguments in this call correspond to the coordinates
    on the screen where the message print should start.
    First argument: line
    Second argument: column
'''


# refresh the screen so that the message is displayed
screen.refresh()

# Request an user input before closing the screen
screen.getch()

# And finally end the window.
''' This last step is essential if we want to exit the `curses` module
 and get bakc to a normal terminal '''
curses.endwin()
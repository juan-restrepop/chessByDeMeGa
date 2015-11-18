'''
    In this tutorial we see some advanced tools
     to 'animate" the display.

    The corresponding youtube tutorial can be found at:
        https://www.youtube.com/watch?v=S1Tel3I2RYU
'''

import curses
import time

screen = curses.initscr()
height, width = screen.getmaxyx()

message = "Let's play some chess!"

q = -1

i, j = 0, 0
horizontal_move = 1
vertical_move = 1

'''
    This time around we will be displaying with a while loop.
    The loop will exit as soon as there is some user input (see line 53).
    We will thus use a `screen.getch()` command. In order to avoid blocking the program
    while waiting for the user input we will need to use the `nodelay()` function:
'''
screen.nodelay(1)

while q < 0:
    screen.clear()
    screen.addstr(i, j, message)
    screen.refresh()

    i += vertical_move
    j += horizontal_move

    # I should change the movements if I reach the limits of the screen
    if i == height - 1:
        vertical_move = -1
    elif i == 0:
        vertical_move = 1

    if j == width - len(message) - 1:
        horizontal_move = -1
    elif j == 0:
        horizontal_move = 1
    # Wait some time before next display
    time.sleep(0.08)

    # And we need to stop the animation as soon as there is user input
    '''
        `getch()` returns an integer
    '''
    q = screen.getch()

screen.getch()
curses.endwin()
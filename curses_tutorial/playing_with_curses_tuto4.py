'''
    In this tutorial we see how to 'animate" the display.

    The corresponding youtube tutorial can be found at:
        https://www.youtube.com/watch?v=7bwK9tsdve4
'''

import curses
import time

screen = curses.initscr()
height, width = screen.getmaxyx()

message = "Let's play some chess!"

for j in range(width - len(message)):
    screen.clear()
    screen.addstr(height/2, j, message)
    screen.refresh()

    # Wait some time before going to the next step in the loop
    time.sleep(0.08)
screen.getch()
curses.endwin()
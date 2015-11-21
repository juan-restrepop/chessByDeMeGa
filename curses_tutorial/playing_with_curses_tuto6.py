'''
    In this tutorial we see how to take into account user input for the movement.

    The corresponding youtube tutorial can be found at:
        https://www.youtube.com/watch?v=RP4slqSu-ck
'''

import curses
import time

screen = curses.initscr()
height, width = screen.getmaxyx()

curses.curs_set(0) # Set it to 0 to make the cursor invisible, 1 visible, and 2 even more visible

message = "Let's play some chess!"

q = -1

i, j = 0, 0
horizontal_move = 1
vertical_move = 1

'''
    We keep playing until user inputs 'q'
'''
while q != ord('q'):
    screen.clear()
    screen.addstr(i, j, message)
    screen.refresh()

    q = screen.getch()

    # counter strike movement keys
    if q == ord('w') and i > 0:
        i += -1
    elif q == ord('s') and i < height - 1:
        i += 1
    elif q == ord('a') and j > 0:
        j += -1
    elif q == ord('d') and j < width - len(message) - 1:
        j += 1

curses.endwin()
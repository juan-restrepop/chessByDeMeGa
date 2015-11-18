'''
    This time we learn how to add color to the display.

    The corresponding youtube tutorial is at:
        https://www.youtube.com/watch?v=1SiXo2uNwAI
'''

import curses
import time


message = raw_input('What message should I display master? ')

screen = curses.initscr()
curses.start_color() # Notice that this call changes to the default color setting
                     # Black background and white text

# Initialize red color
curses.init_color(1, 1000, 0, 0)
# Initialize green color
curses.init_color(2, 0, 1000, 0)
# Initialize blue color
curses.init_color(3, 0, 0, 1000)
# Initialize black color
curses.init_color(4, 0, 0, 0)
# Initialize gray color
curses.init_color(5, 550, 550, 550)


## Now we can initialize some color pairs
# red foreground and blue background
curses.init_pair(1, 1, 3)

# green foreground and red background
curses.init_pair(2, 2, 1)

#gray foreground and black background
curses.init_pair(3, 4, 5)

height, width = screen.getmaxyx()

q = -1

i, j = 0, 0
horizontal_move = 1
vertical_move = 1

screen.nodelay(1)

while q < 0:
    screen.clear()
    screen.addstr(i, j, message, curses.color_pair((i + j) % 3 + 1))
    screen.refresh()

    i += vertical_move
    j += horizontal_move

    if i == height - 1:
        vertical_move = -1
    elif i == 0:
        vertical_move = 1

    if j == width - len(message) - 1:
        horizontal_move = -1
    elif j == 0:
        horizontal_move = 1

    time.sleep(0.3)
    q = screen.getch()

screen.getch()
curses.endwin()
'''
    In this tutorial we see how to 'position' the message to be displayed.

    The corresponding youtube tutorial can be found at:
        https://www.youtube.com/watch?v=YsmIRm0Uxq8
'''
import curses
screen = curses.initscr()

message = "Let's play some chess!"

i_coordinates = [0, 2, 6]
j_coordinates = [0, 2, 6]

for i, j in zip(i_coordinates, j_coordinates):
    screen.addstr(i, j, message)
    screen.refresh()
    screen.getch()

# We can also get the actual size of the terminal window at play
height, width = screen.getmaxyx()

screen.addstr(height/2, width/2, message)
screen.refresh()
screen.getch()

curses.endwin()

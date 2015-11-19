import curses
from curses import endwin as close_cursed_screen

def rgb_to_curses_color(color):
     return color[0]*1000/255, color[1]*1000/255, color[2]*1000/255

## Colors for display
white_square_rgb = (255, 0, 0)
black_square_rgb = (0, 0, 255)
white_piece_rgb = (0, 0, 0)
black_piece_rgb = (255, 255, 255)

## Initialize the screen
screen = curses.initscr()
curses.start_color()
height, width = screen.getmaxyx()

## Initialize colors
# Board  white squares
curses.init_color(1, rgb_to_curses_color(white_square_rgb)[0], rgb_to_curses_color(white_square_rgb)[1], rgb_to_curses_color(white_square_rgb)[2])
# Board black squares
curses.init_color(2, rgb_to_curses_color(black_square_rgb)[0], rgb_to_curses_color(black_square_rgb)[1], rgb_to_curses_color(black_square_rgb)[2])
# White piece
curses.init_color(3, rgb_to_curses_color(white_piece_rgb)[0], rgb_to_curses_color(white_piece_rgb)[1], rgb_to_curses_color(white_piece_rgb)[2])
# Black piece
curses.init_color(4, rgb_to_curses_color(black_piece_rgb)[0], rgb_to_curses_color(black_piece_rgb)[1], rgb_to_curses_color(black_piece_rgb)[2])

## Initialize necessary color pairs
# Black piece on white square
curses.init_pair(1, 4, 1)
# Black piece on black square
curses.init_pair(2, 4, 2)
# White piece on white square
curses.init_pair(3, 3, 1)
# White piece on black square
curses.init_pair(4, 3, 2)

def get_piece_color(piece):
    i, j = piece.coordinates
    square_color = ((j + i) % 2)

    if piece.color == 'b' and square_color == 0:
        return 1
    elif piece.color == 'b' and square_color == 1:
        return 2
    elif piece.color == 'w' and square_color == 0:
        return 3
    elif piece.color == 'w' and square_color == 1:
        return 4

    return

def screen_small_empty_board(Board):
    screen.clear()

    board_columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    board_lines = ['8', '7', '6', '5', '4', '3', '2', '1']

    i_0, j_0 = 1, 2

    for i in range(8):
        screen.addstr(i_0 + i, 0, board_lines[i])
        for j in range(8):
            screen.addstr(0, j_0 + j, board_columns[j])
            color = Board.get_square_color(i, j) + 1
            screen.addstr(i_0 + i, j_0 + j, ' ', curses.color_pair(color))

    screen.move(height - 1, width - 1)

def print_small_cursed_board(Board):

    screen_small_empty_board(Board)

    i_0, j_0 = 1, 2
    for piece in Board.get_all_pieces():
        i, j = piece.coordinates
        color = get_piece_color(piece)

        screen.addstr(i_0 + i, j_0 + j, piece.kind, curses.color_pair(color))

    screen.move(height - 1, width - 1)
    screen.refresh()
    screen.getch()
    close_cursed_screen()










"""The idea behind the project is to use a iterative process that will go through all possible steps that can be taken
and will return the correct solution

The game used is a game where you have to place several pieces inside a grid (see documentation for images)
The starting grid is given, and after this you will have to be able to solve the puzzle
grid is 11x5
"""
import tkinter
import numpy as np

# definitions
dag = np.array([[1, 1, 0, 0],  # dark green
                [0, 1, 1, 1, ]])
ora = np.array([[1, 0, 0],
                [1, 1, 1]])  # orange
red = np.array([[1, 1, 0],
                [1, 1, 1]])  # red
lib = np.array([[1, 1, 1],
                [0, 0, 1],
                [0, 0, 1]])  # light blue
gre = np.array([[0, 1, 0],
                [1, 1, 1],
                [0, 1, 0]])  # grey
pur = np.array([[1, 1, 1, 1]])  # purple
dab = np.array([[0, 1],
                [0, 1],
                [0, 1],
                [1, 1]])  # dark blue
bei = np.array([[1, 1, 1, 0],
                [0, 0, 1, 0]])  # beige
pin = np.array([[1, 1, 0],
                [0, 1, 1, ],
                [0, 0, 1]])  # pink
whi = np.array([[1, 0],
                [1, 1]])  # white
yel = np.array([[1, 1],
                [0, 1],
                [1, 1]])  # yellow
lig = np.array([[1, 1],
                [1, 1]])  # light green

gui_piece_selected = True
master = tkinter.Tk()
option_buttons_column = 20  # constant
grid = [[]]
starting_pieces = []


def get_piece_string():
    global gui_piece_selected
    if gui_piece_selected:
        return "  -  "
    else:
        return "      "


def generate_field():
    master.title("fill in the correct level")
    master.geometry("650x375")
    buttons = []
    for y in range(0, 5):
        rowButtons = []
        for x in range(0, 11):
            btn_text = tkinter.StringVar()
            btn_text.set(get_piece_string())
            button = tkinter.Button(master, textvariable=btn_text,
                                    command=lambda l_x=x, l_y=y, l_txt=btn_text: button_callback(l_x, l_y, l_txt))
            button.grid(row=y, column=x)
            rowButtons.append(0)
        buttons.append(rowButtons)
    return buttons


def bool2int(given_bool):
    if given_bool:
        return 1
    else:
        return 0


def button_callback(x: int, y: int, btn_text):
    global grid
    grid[y][x] = bool2int(gui_piece_selected)
    btn_text.set(get_piece_string())


def generate_option_buttons():
    # standard piece, wizard, hat, empty
    piece_button = tkinter.Button(master, text="piece", command=lambda: put_piece())
    piece_button.grid(row=0, column=option_buttons_column)
    no_piece_button = tkinter.Button(master, text="empty", command=lambda: dont_put_piece())
    no_piece_button.grid(row=1, column=option_buttons_column)
    calculate_button = tkinter.Button(master, text="calculate", command=lambda: calculate())
    calculate_button.grid(row=2, column=option_buttons_column + 1)

def generate_pieces_left():
    row_int = 0
    pieces_label = tkinter.Label(master,text="Select the pieces that are left")
    pieces_label.grid(row = row_int,column=option_buttons_column+2)
    row_int += 1
    dag_button = tkinter.Button(master,text="Dark Green",command=lambda: add_dag_piece())
    dag_button.grid(row=row_int,column=option_buttons_column+2)
    row_int += 1
    ora_button = tkinter.Button(master, text="Orange",command=lambda: add_lig_piece())
    ora_button.grid(row=row_int, column=option_buttons_column + 2)
    row_int += 1
    red_button = tkinter.Button(master, text="Red",command=lambda: add_red_piece())
    red_button.grid(row=row_int, column=option_buttons_column + 2)
    row_int += 1
    lib_button = tkinter.Button(master, text="Light Blue",command=lambda: add_lib_piece())
    lib_button.grid(row=row_int, column=option_buttons_column + 2)
    row_int += 1
    gre_button = tkinter.Button(master, text="Grey",command=lambda: add_gre_piece())
    gre_button.grid(row=row_int, column=option_buttons_column + 2)
    row_int += 1
    pur_button = tkinter.Button(master, text="Purple",command=lambda: add_pur_piece())
    pur_button.grid(row=row_int, column=option_buttons_column + 2)
    row_int += 1
    dab_button = tkinter.Button(master, text="Dark Blue",command=lambda: add_dab_piece())
    dab_button.grid(row=row_int, column=option_buttons_column + 2)
    row_int += 1
    bei_button = tkinter.Button(master, text="Beige",command=lambda: add_bei_piece())
    bei_button.grid(row=row_int, column=option_buttons_column + 2)
    row_int += 1
    pin_button = tkinter.Button(master, text="Pink",command=lambda: add_pin_piece())
    pin_button.grid(row=row_int, column=option_buttons_column + 2)
    row_int += 1
    whi_button = tkinter.Button(master, text="White",command=lambda: add_whi_piece())
    whi_button.grid(row=row_int, column=option_buttons_column + 2)
    row_int += 1
    yel_button = tkinter.Button(master, text="Yellow",command=lambda: add_yel_piece())
    yel_button.grid(row=row_int, column=option_buttons_column + 2)
    row_int += 1
    lig_button = tkinter.Button(master,text="Light Green",command=lambda: add_lig_piece())
    lig_button.grid(row=row_int,column=option_buttons_column+2)

def add_dag_piece():
    global starting_pieces
    starting_pieces.append(dag)

def add_ora_piece():
    global starting_pieces
    starting_pieces.append(ora)

def add_red_piece():
    global starting_pieces
    starting_pieces.append(red)

def add_lib_piece():
    global starting_pieces
    starting_pieces.append(lib)

def add_gre_piece():
    global starting_pieces
    starting_pieces.append(gre)

def add_pur_piece():
    global starting_pieces
    starting_pieces.append(pur)

def add_dab_piece():
    global starting_pieces
    starting_pieces.append(dab)

def add_bei_piece():
    global starting_pieces
    starting_pieces.append(bei)

def add_pin_piece():
    global starting_pieces
    starting_pieces.append(pin)

def add_whi_piece():
    global starting_pieces
    starting_pieces.append(whi)

def add_yel_piece():
    global starting_pieces
    starting_pieces.append(whi)

def add_lig_piece():
    global starting_pieces
    starting_pieces.append(lig)

def put_piece():
    global gui_piece_selected
    gui_piece_selected = True


def dont_put_piece():
    global gui_piece_selected
    gui_piece_selected = False


def build_gui():
    global grid, gui_piece_selected
    gui_piece_selected = False
    grid = generate_field()
    generate_option_buttons()
    generate_pieces_left()
    master.mainloop()


###### calculation part##########
class Node:
    def __init__(self, state, pieces: list):
        self.state = state
        self.pieces = pieces
        if check_if_solution_found(node=self):
            print("The solution has been found")
            exit(99)
        find_valid_moves(node=self)


def check_if_solution_found(node):
    # loop through all pieces and if none are 0, the solution is found
    for y in range(len(node.state)):
        for x in range(len(node.state[y])):
            if node.state[y][x] == 0:
                return False
    # if no empty spaces were found, the game is finished
    return True


def find_valid_moves(node):
    # loop through all the available pieces and try to place them in any valid position
    # if they can be placed in the new position create a new node and remove the piece from the available piece list

    for piece_pos in range(0,len(node.pieces)):
        piece = node.pieces[piece_pos]
        #piece can be placed with two faces up, the 1 in the flip signifies the axis over which we flip
        for flip in range(2):
            piece = np.flip(piece,1)
            for rot in range(0, 5):
                # try to place the piece in every possible rotation,
                # we will rotate it 4 times in the last iteration, not that efficient but ez to write
                piece = np.rot90(piece)
                for y in range(len(node.state)):
                    for x in range(len(node.state[y])):
                        if piece_can_be_placed(piece, node.state, x, y):
                            new_state = execute_step(piece, node.state, x, y)
                            new_pieces = node.pieces.copy()
                            new_pieces.pop(piece_pos)  # removes and returns the element at the given index
                            Node(new_state, new_pieces)


def piece_can_be_placed(piece, state, x, y):
    try:
        for piece_y in range(len(piece)):
            for piece_x in range(len(piece[piece_y])):
                if piece[piece_y][piece_x] != 0:
                    # we are trying to place a piece here -> check if this place is available on the board
                    if state[y + piece_y][x + piece_x] != 0:
                        # the place isn't available (the y and x is the offset where we are trying to place the piece
                        return False
        # no unavailable places found -> the piece can be placed
        return True
    except IndexError as ind:
        #we tried to place a piece of the board pretty much -> place won't fit anyways
        return False



def execute_step(piece, state, x, y):
    for piece_y in range(len(piece)):
        for piece_x in range(len(piece[piece_y])):
            # change the values in the state to the corresponding value from the piece, if the value was 1
            # if was zero no piece was trying to be placed
            if piece[piece_y][piece_x] != 0:
                state[piece_y + y][piece_x + x] = piece[piece_y][piece_x]
    return state


def render(board):
    print("#" * 30)
    row_str = ""
    for y in range(len(board)):
        for x in range(len(board[y])):
            row_str += str(board[y][x]) + "  "
        print(row_str)
        row_str = ""
    print("#" * 30)


def calculate():
    global grid, starting_pieces
    if len(starting_pieces) == 0:
        print("There were no starting pieces given, you probably still need to configure this")
    # start the first node, this will trigger the iterative process
    Node(grid, starting_pieces)

def calculate_one_left():
    grid_loc = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    pieces_loc = [dag]
    Node(grid_loc,pieces_loc)

def calculate_empty():
    grid_loc = []
    for y in range(0, 5):
        row_lst = []
        for x in range(11):
            row_lst.append(0)
        grid_loc.append(row_lst)
    pieces_loc = [dag, ora, red, lib, gre, pur, dab, bei, pin, whi, yel, lig]
    Node(grid_loc, pieces_loc)


# main
# pieces: standard piece -> 1, wizard -> 20, hat -> 10, empty -> 0, double_stack -> 2

build_gui()
#calculate_empty()
#calculate_one_left()
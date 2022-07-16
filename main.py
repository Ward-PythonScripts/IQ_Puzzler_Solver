"""The idea behind the project is to use a iterative process that will go through all possible steps that can be taken
and will return the correct solution

The game used is a game where you have to place several pieces inside a grid (see documentation for images)
The starting grid is given, and after this you will have to be able to solve the puzzle
grid is 11x5
"""
import tkinter
#definitions
dag = [[1,1,0,0],     #green
     [0,1,1,1,]]
ora = [[1,0,0],
     [1,1,1]]   #orange
red = [[1,1,0],
     [1,1,1]]   #red
lib = [[1,1,1],
     [0,0,1],
     [0,0,1]]   #light blue
gre = [[0,1,0],
     [1,1,1],
     [0,1,0]]   #grey
pur = [[1,1,1,1]] #purple
dab = [[0,1],
     [0,1],
     [0,1],
     [1,1]] #dark blue
bei = [[1,1,1,0],
       [0,0,1,0]] #beige
pin = [[1,1,0],
       [0,1,1,],
       [0,0,1]] #pink
whi = [[1,0],
       [1,1]]   #white
yel = [[1,1],
       [0,1],
       [1,1]] #yellow
lig = [[1,1],
       [1,1]] #light green


gui_piece_selected = True
master = tkinter.Tk()
option_buttons_column = 20  # constant
grid = [[]]

def get_piece_string():
    global gui_piece_selected
    if gui_piece_selected:
        return "  -  "
    else:
        return "      "

def generate_field():
    master.title("fill in the correct level")
    master.geometry("450x175")
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

def button_callback(x:int, y:int, btn_text):
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
    master.mainloop()


def calculate():
    pass

# main
# pieces: standard piece -> 1, wizard -> 20, hat -> 10, empty -> 0, double_stack -> 2

build_gui()


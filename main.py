"""The idea behind the project is to use a iterative process that will go through all possible steps that can be taken
and will return the correct solution

The game used is a game where you have to place several pieces inside a grid (see documentation for images)
"""

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

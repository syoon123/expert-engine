from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r")
    line = f.readline()
    scr = new_screen()
    color = [0,255,0]
    
    while (line != ""):
        command = line.strip("\n")
        args = f.readline().strip("\n").split(" ")

        if (command == "line"):
            add_edge(points, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]))
            print "line added"

        if (command == "display"):
            clear_screen(scr)
            draw_lines(points, scr, color)
            display(scr)
            print "displaying"

        if (command == "ident"):
            ident(transform)
            print "reset transformation matrix"

        if (command == "scale"):
            temp = make_scale(int(args[0]), int(args[1]), int(args[2]))
            matrix_mult(temp, transform)
            print "scaling"

        if (command == "rotate"): 
            
            if (args[0] == "x"):
                temp = make_rotX(int(args[1]))

            if (args[0] == "y"):
                temp = make_rotY(int(args[1]))

            if (args[0] == "z"):
                temp = make_rotZ(int(args[1]))

            matrix_mult(temp, transform)
            print "rotating"

        if (command == "move"):
            temp = make_translate(int(args[0]), int(args[1]), int(args[2]))
            matrix_mult(temp, transform)
            print "translating"

        if (command == "apply"):
            matrix_mult(transform, points)
            print "applying transformation matrix"

        if (command == "save"):
            clear_screen(scr)
            draw_lines(points, scr, color)
            save_extension(scr, args[0])
            print "saving"

        line = f.readline()
        

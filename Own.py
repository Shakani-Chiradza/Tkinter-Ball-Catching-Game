from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font


canvas_width = 1000
canvas_height = 600

root = Tk()  # create window

c = Canvas(root, width=canvas_width, height=canvas_height, background='red4')  # specify window specs
c.create_polygon(0,610,50,500,100,590,150,500,200,590,250,500,300,590,350,500,400,610, fill='orange2')
c.create_polygon(0,610,50,550,100,610,150,550,200,610,250,550,300,610,350,550,400,610, fill='yellow')
c.create_polygon(0,610,50,590,100,610,150,590,200,610,250,590,300,610,350,590,400,610, fill='orange2')
c.pack()


root.mainloop()  # pauses screen so it doesn't disappear too fast



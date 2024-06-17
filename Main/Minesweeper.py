from tkinter import *
from tkinter import ttk
import settings 
import utils 
from cells import Cell
# Opens up a window all code goes inbetween
root = Tk()

# Overide the windoiws settings
root.configure(bg='gray')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper')
root.resizable(False, False)

# What difficulty do you want?
middle_frame = Frame(
    root,
    bg = 'blue',
    width = utils.width_prct(50),
    height = utils.height_prct(50)
)
middle_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))

top_frame = Frame(
    root,
    bg = 'dark grey',
    width = utils.width_prct(100),
    height = utils.height_prct(10)
)
top_frame.place(x=0, y=0)

game_frame = Frame(
    root,
    bg = 'black',
    width = utils.width_prct(100),
    height = utils.height_prct(100)
)
game_frame.place(x=utils.width_prct(0), y=utils.height_prct(10))

for x in range(settings.GRID_SIZE_x):
    for y in range(settings.GRID_SIZE_y):
        c = Cell()
        c.Create_btn_object(game_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

# Run window
root.mainloop()
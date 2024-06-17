from tkinter import Button



class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None

    def Create_btn_object(self, location):
        btn = Button(
            location,
            text='text'
        )
        btn.bind('<Button-1>', self.left_click_actions ) # Left Click
        btn.bind('<Button-3>', self.right_click_actions ) # Right Click
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print(event)
        print('Left clicked!')

    def right_click_actions(self, event):
        print(event)
        print('Right clicked!')
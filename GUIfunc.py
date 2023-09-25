import tkinter as tk
import data
import matrix as m
import copy
from score import Score

def update_grid(self):
        whip = 15
        for i in range(4):
            for j in range(4):
                value = self.matrix[i][j]
                if value != 0:
                    self.grid_tiles[whip].configure(
                        text = str(value), 
                        bg = data.background_color_tiles[self.matrix[i][j]],
                        fg = data.number_color_tiles[self.matrix[i][j] ])
                else:
                    self.grid_tiles[whip].configure(
                        text = "",
                        bg = data.background_color_empty,
                        )
                whip -= 1
                    
def swipe(self, event):
    key = event.keysym
    state = copy.deepcopy(self.matrix)
    match (key):
        case "Escape": exit()
        case "Up":
            print("Up")
            self.matrix, self.score = m.swipe_up(self.matrix, self.score)
            if state != self.matrix:
                self.matrix = m.generate_tile(self.matrix)
                update_grid(self)
        case "Down":
            print("Down")
            self.matrix, self.score = m.swipe_down(self.matrix, self.score)
            if state != self.matrix:
                self.matrix = m.generate_tile(self.matrix)
                update_grid(self)
        case "Right":
            print("Right")
            self.matrix, self.score = m.swipe_right(self.matrix, self.score)
            if state != self.matrix:
                self.matrix = m.generate_tile(self.matrix)
                update_grid(self)
        case "Left":
            print("Left")
            self.matrix, self.score = m.swipe_left(self.matrix, self.score)
            if state != self.matrix:
                self.matrix = m.generate_tile(self.matrix)
                update_grid(self) 
    game_state(self)
    update_score(self) 

    print(self.matrix)   

def help_button():
    helper = tk.Toplevel()
    helper.title("manual")
    helper.geometry("300x300")
    tk.Label(helper,
            text = "HOW TO PLAY: Use your arrow keys to move the tiles. Tiles with the same number merge into one when they touch. Add them up to reach 2048!", 
            font = data.font2,
            wraplength= 200).pack(expand=True, fill='y')
    tk.Button(
        helper, 
        text="Ok", 
        bd = 1, 
        font = data.font2, 
        command = helper.destroy).pack(expand=True, fill='both')
        
def new_game_button(self):
    helper = tk.Toplevel()
    helper.title("Sure?")
    helper.geometry("300x300")
    
    tk.Label(
        helper,
        text="Are you sure? You will lose your progress",
        font=data.font2,
        wraplength=200
    ).place(x = 0, y = 0, relheight = 0.5, relwidth = 1)
    
    tk.Button(
        helper,
        text = "No",
        bd = 1,
        font = data.font2,
        command = helper.destroy
    ).place(relx = 0, rely = 0.5, relheight = 0.5, relwidth = 0.5)
    
    tk.Button(
        helper,
        text = "Yes",
        bd = 1,
        font = data.font2,
        command = lambda: new_game(self, helper)
    ).place(relx = 0.5, rely = 0.5, relheight = 0.5, relwidth = 0.5)

        
def new_game(self, wind):
    self.score = 0
    update_score(self)
    self.matrix = m.new_game()
    self.bind("<Key>", lambda event: swipe(self, event))
    update_grid(self)
    self.winner = False
    wind.destroy()

def continue_game(self, wind):
    self.bind("<Key>", lambda event: swipe(self, event))
    update_grid(self)
    wind.destroy()

def game_state(self):
    if m.win(self.matrix) and not self.winner:
        self.winner = True
        self.unbind("<Key>")
        helper = tk.Toplevel()
        helper.title("Sure?")
        helper.geometry("300x300")
    
        tk.Label(
            helper,
            text="YOU WON, do you want to continue?",
            font=data.font2,
            wraplength=200
        ).place(x = 0, y = 0, relheight = 0.5, relwidth = 1)
        
        tk.Button(
            helper,
            text = "Yes",
            bd = 1,
            font = data.font2,
            command = lambda: continue_game(self, helper)
        ).place(relx = 0, rely = 0.5, relheight = 0.5, relwidth = 0.5)
        
        tk.Button(
            helper,
            text = "No",
            bd = 1,
            font = data.font2,
            command = lambda: new_game(self, helper)
        ).place(relx = 0.5, rely = 0.5, relheight = 0.5, relwidth = 0.5)
    
    if m.loss(self.matrix):
        self.unbind("<Key>")
        helper = tk.Toplevel()
        helper.title("Sure?")
        helper.geometry("300x300")
    
        tk.Label(
            helper,
            text="YOU LOST :(",
            font=data.font2,
            wraplength=200
        ).place(x = 0, y = 0, relheight = 0.5, relwidth = 1)
        
        tk.Button(
            helper,
            text = "New game",
            bd = 1,
            font = data.font2,
            command = lambda: new_game(self, helper)
        ).place(relx = 0, rely = 0.5, relheight = 0.5, relwidth = 1)

def update_score(self):
    scr = Score(self.score, self.score_value, self.best_score_value)
    scr.get_score()

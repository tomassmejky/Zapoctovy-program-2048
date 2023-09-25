import tkinter as tk
import data
import matrix as m
import GUIfunc as g

class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('2048')
        self.resizable(0, 0)
        self.init_info()
        self.grid_tiles = self.init_grid()
        self.winner = False
        self.score = 0
        self.matrix = m.new_game()
        self.bind("<Key>", lambda event: g.swipe(self, event))
        print(self.matrix)
        g.update_grid(self)
        self.mainloop()
        

    def init_info(self):
        top = tk.Frame(self)
        top.place(x = 0, y = 0, relheight=0.28, relwidth=1)

        label1 = tk.Label(
            top, 
            text="2048", 
            font = data.font1, 
            fg = data.text_color)
        
        label2 = tk.Label(
            top, 
            text="Join the tiles, get to 2048!", 
            font = data.font2, 
            fg = data.text_color)
        
        help_but = tk.Button(
            top, 
            text = "How to play", 
            font = data.font3, bd = 0, 
            activebackground = data.background_color,
            command = g.help_button)
        
        new_game_but = tk.Button(
            top, 
            text= "New Game", 
            bd = 0, 
            bg = data.text_color,  
            font = data.font4, 
            fg = 'white', 
            padx = 10, 
            pady = 10,
            command = lambda: g.new_game_button(self)
            )
        
        score_display = tk.Label(
            top, 
            text = "SCORE", 
            font = data.font2, 
            fg = data.text_color)
        
        best_score = tk.Label(
            top, 
            text = "BEST", 
            font = data.font2, 
            fg = data.text_color)
        
        self.score_value = tk.Label(
            top, 
            text = "0", 
            font = data.font2, 
            fg = data.text_color)
        
        self.best_score_value = tk.Label(
            top, 
            text = "0", 
            font = data.font2, 
            fg = data.text_color)
        
        label1.place(x = 0, y = 0)
        label2.place(x = 0, rely = 0.5)
        help_but.place(x = 0, rely = 0.65)
        new_game_but.place(x = 350, rely = 0.6)
        score_display.place(x = 300, y = 0)
        self.score_value.place(x = 300,  y = 20)
        best_score.place(x = 400)
        self.best_score_value.place(x = 400, y = 20)

    def init_grid(self):
        tiles = tk.Frame(self, background = data.background_grid_color, width=500, height=500)
        tiles.grid(pady=200)

        for i in range(4):
            for j in range(4):
                cell = tk.Label(
                    tiles,
                    text="",
                    bg = data.background_color_empty,
                    width = 5,
                    height = 3,
                    justify = tk.CENTER,
                    font= data.font5
                )
                cell.grid(
                    row=i,
                    column=j,
                    padx = 10,
                    pady= 10
                )
        return tiles.grid_slaves()
    

game = Game()



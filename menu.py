import tkinter as tk
from tkinter import ttk

BAKCGROUND_COLOR = "#1A1A1A"
FOREGROUND_COLOR = "#FFFFFF"
LIGHT_GRAY = "#D3D3D3"
BLUE = "#0000FF"
YELLOW = "#FFFF00"
class Menu:
    def __init__(self, onclick):
        self.onclick = onclick
        self.root = self.__create_root()
        self.addr_entry, self.entry_value = self.__create_entry()
        self.color_buttons, self.team_color = self.__create_rbtn_colors()
        self.robots_buttons, self.robot_index = self.__create_rbtn_robots()
        self.start_button = self.__create_btn_start()

    def __create_root(self):
        root = tk.Tk()
        root.config(padx=5, pady=5, background=BAKCGROUND_COLOR)
        root.resizable(False, False)
        root.title("VSSS Game")
        return root
    
    def __create_entry(self):
        ##titulo do input
        text = tk.Label(self.root, text="IP DO SERVIDOR:")
        text.config(fg=FOREGROUND_COLOR, bg=BAKCGROUND_COLOR, justify=tk.LEFT)
        text.pack(padx=(25,0), pady=(25,0), side=tk.TOP, anchor=tk.NW)

        ##input
        text = tk.StringVar(self.root, "")
        entry = tk.Entry(self.root) 
        entry.config(
            bg=BAKCGROUND_COLOR, 
            fg=FOREGROUND_COLOR, 
            highlightthickness=1,
            relief=tk.SOLID, 
            highlightcolor=FOREGROUND_COLOR,
            highlightbackground=FOREGROUND_COLOR,
            textvariable = text
        )
        entry.pack(padx=25, pady=5, fill=tk.X, expand=1)
        return entry, text
    
    def __create_rbtn_colors(self):
        ##titulo dos botoes
        text = tk.Label(self.root, text="TIME:")
        text.config(fg=FOREGROUND_COLOR, bg=BAKCGROUND_COLOR, justify=tk.LEFT)
        text.pack(padx=(25,0), pady=(10,0),side=tk.TOP, anchor=tk.NW)

        ##botoes 
        frame = tk.Frame(self.root, bg=BAKCGROUND_COLOR)
        color = tk.StringVar(self.root, "AZUL")
        button_blue = tk.Radiobutton(frame)
        button_blue.config(
            highlightbackground = BLUE,
            relief=tk.FLAT,
            indicator=0,
            variable=color,
            value="AZUL",
            height=3,
            fg=FOREGROUND_COLOR,
            bg=BAKCGROUND_COLOR,
            selectcolor=BLUE,
            cursor="hand2"
        )
        
        button_yellow = tk.Radiobutton(frame)
        button_yellow.config(
            highlightbackground = YELLOW,
            relief=tk.SOLID,
            indicator=0,
            variable=color,
            value="AMARELO",
            height=3,
            fg=FOREGROUND_COLOR,
            bg=BAKCGROUND_COLOR,
            selectcolor=YELLOW,
            cursor="hand2"
        )

        frame.pack(side=tk.TOP, padx=25, fill=tk.X)
        button_blue.pack(side=tk.LEFT, padx=(0,5), fill=tk.X, expand=1)
        button_yellow.pack(side=tk.RIGHT, padx=(5,0), fill=tk.X, expand=1)

        return [[button_blue, button_yellow], color]
    
    def __create_rbtn_robots(self):
        ##titulo dos botoes
        text = tk.Label(self.root, text="ROBO:")
        text.config(fg=FOREGROUND_COLOR, bg=BAKCGROUND_COLOR, justify=tk.LEFT)
        text.pack(padx=(25,0), pady=(10,0),side=tk.TOP, anchor=tk.NW)

        ##botoes
        frame = tk.Frame(self.root, bg=BAKCGROUND_COLOR)
        index = tk.IntVar(self.root, 0)
        
        self.images = [
            tk.PhotoImage(file="sprites/robo0.png"),
            tk.PhotoImage(file="sprites/robo1.png"),
            tk.PhotoImage(file="sprites/robo2.png")
        ]

        robot_0 = tk.Radiobutton(frame)
        robot_0.config(
            image=self.images[0],
            overrelief=tk.SOLID,
            offrelief=tk.FLAT,
            borderwidth=3,
            indicator=0,
            variable=index,
            selectcolor="red",
            value=0,
            cursor="hand2"
        )

        robot_1 = tk.Radiobutton(frame)
        robot_1.config(
            image=self.images[1],
            overrelief=tk.SOLID,
            offrelief=tk.FLAT,
            borderwidth=3,
            indicator=0,
            variable=index,
            selectcolor="red",
            value=1,
            cursor="hand2"
        )
        robot_2 = tk.Radiobutton(frame)
        robot_2.config(
            image=self.images[2],
            overrelief=tk.SOLID,
            offrelief=tk.FLAT,
            borderwidth=3,
            variable=index,
            indicator=0,
            value=2,
            selectcolor="red",
            cursor="hand2"
        )

        frame.pack(side=tk.TOP, padx=25,  fill=tk.X)
        robot_0.pack(side=tk.LEFT, padx=(0,5), fill=tk.X, expand=1)
        robot_1.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=1)
        robot_2.pack(side=tk.RIGHT, padx=(5,0), fill=tk.X, expand=1)

        return [[robot_0, robot_1, robot_2], index]

    def start(self):
        print(f"IP {self.entry_value.get()}; TIME {self.team_color.get()} ROBO {self.robot_index.get()}")
        self.onclick(self.entry_value.get(), self.team_color.get(), self.robot_index.get())

    def __create_btn_start(self):
        ##create button
        button = tk.Button(self.root)
        button.config(
            relief=tk.FLAT,
            text="COMEÇAR",
            bg=LIGHT_GRAY,
            fg=BAKCGROUND_COLOR,
            highlightthickness = 0,
            cursor="hand2",
            command=self.start
        )

        button.pack(side=tk.TOP, fill=tk.X, expand=1, padx=25, pady=25)
    
    
    def show(self):
        self.root.deiconify()
    
    
    def hide(self):
        self.root.withdraw()

    def run(self):
        self.root.mainloop()

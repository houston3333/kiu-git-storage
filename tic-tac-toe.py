from check import noneCounter, victory_check, state
from tkinter import *
from tkinter import messagebox


SIGN_X = 'X'
SIGN_O = 'O'


buttons = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]


def clean_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].configure(text = "")
            buttons[i][j]["state"] = NORMAL
            state[i][j] = None


def insert(i,j,current_sign):
    buttons[i][j].configure(text = current_sign)
    buttons[i][j]["state"] = DISABLED
    state[i][j] = current_sign
    

def click(i,j):
    current_sign = SIGN_O if noneCounter() % 2 == 0 else SIGN_X
    title_sign = SIGN_O if current_sign == SIGN_X else SIGN_X    

    insert(i,j,current_sign)
    
    if noneCounter() > 0:
        title = Label(gui, text= f'Ходит {title_sign}', font= ("Arial", 11, "bold")).grid(row= 3, column= 1)
    else:
        title = Label(gui, text= "Game Over", font= ("Arial", 9, "bold")).grid(row= 3, column= 1)
        result = messagebox.showinfo("Game Over", "DRAWN GAME")
        title = Label(gui, text= "Start", width = 5, font= ("Arial", 14, "bold")).grid(row= 3, column= 1)
        clean_buttons()

    if victory_check() == True:
        title = Label(gui, text= "Game Over", font= ("Arial", 9, "bold")).grid(row= 3, column= 1)
        result = messagebox.showinfo("Game Over", f"!!!{current_sign} WIN!!!") 
        title = Label(gui, text= "Start", width = 5, font= ("Arial", 14, "bold")).grid(row= 3, column= 1)
        clean_buttons()
    gui.update()
    

def main():
    global gui
    gui = Tk(className="tic-tac-toe")
    gui.geometry("230x290")

    for i in range(3):
        for j in range(3):                   
            buttons[i][j] = Button(height = 2, width = 4, bg = '#9370D8',font = ("Arial", 20, "bold"), command = lambda x = i, y = j : click(x,y))
            buttons[i][j].grid(row = i, column = j)
    
    global title
    title = Label(gui, text= "Start", font= ("Arial", 14, "bold")).grid(row= 3, column= 1)

    gui.mainloop()


if __name__ == "__main__":
    main()
from random import *
from tkinter import *
from time import *
import tkinter.ttk

sudoku = []  # stores a copy of the board.

l = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # each row of the board.

for i in range(9):
    sudoku.append(l.copy())  # to store in different addresses

s = []

for i in sudoku:
    s.append(i.copy())

block = {}

r, c = -1, -1

block_num = 0


def fillblock1():
    global s
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(3):
        for j in range(3):
            a = choice(List)
            s[i][j] = a
            List.remove(a)


def fillblock5():
    global s
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(3, 6):
        for j in range(3, 6):
            a = choice(List)
            s[i][j] = a
            List.remove(a)


def fillblock9():
    global s
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(6, 9):
        for j in range(6, 9):
            a = choice(List)
            s[i][j] = a
            List.remove(a)


fillblock1()
# returns the position of an empty square if available


def getemptypos():
    for i in range(9):
        for j in range(9):
            if s[i][j] == 0:
                return i, j
    return -1, -1

# returns the values in a block


def getBlock(r, c):

    B = []  # storing the values in the block

    if r < 3:
        if c < 3:
            for i in range(3):
                for j in range(3):
                    B.append(s[i][j])
        elif c < 6:
            for i in range(3):
                for j in range(3, 6):
                    B.append(s[i][j])
        else:
            for i in range(3):
                for j in range(6, 9):
                    B.append(s[i][j])
    elif r < 6:
        if c < 3:
            for i in range(3, 6):
                for j in range(3):
                    B.append(s[i][j])
        elif c < 6:
            for i in range(3, 6):
                for j in range(3, 6):
                    B.append(s[i][j])
        else:
            for i in range(3, 6):
                for j in range(6, 9):
                    B.append(s[i][j])
    else:
        if c < 3:
            for i in range(6, 9):
                for j in range(3):
                    B.append(s[i][j])
        elif c < 6:
            for i in range(6, 9):
                for j in range(3, 6):
                    B.append(s[i][j])
        else:
            for i in range(6, 9):
                for j in range(6, 9):
                    B.append(s[i][j])

    return B

# returns true if ele can be added to row r and column c.


def canbeadded(ele, r, c):
    row = []  # to store values in rth row
    column = []  # to store values in cth column
    block = []  # to store values in the block

    for i in range(9):
        row.append(s[r][i])
        column.append(s[i][c])
    # getting the values present the the rth row in list row and cth coloum in list column

    block = getBlock(r, c)

    return ele not in row and ele not in column and ele not in block

# implements backtracking to solve the puzzle


def solvable(s):

    r, c = getemptypos()

    if r == -1 and c == -1:
        return True  # Solution complete -> exit condition

    for i in range(1, 10):
        if canbeadded(i, r, c):
            s[r][c] = i
            if solvable(s):
                return True
            s[r][c] = 0

    return False


solvable(s)


def PrintBoard():
    for i in range(9):
        print(s[i])


# interface using tkinter
diff_level = 0


def makegame():
    if diff_level == 0:
        exit()
    for i in range(9):
        indexes = sample(range(9), 8)
        for j in indexes:
            sudoku[i][j] = s[i][j]


def set_difficulty(window, value):
    global diff_level
    diff_level = value
    window.destroy()


def difficulty_window():
    window = Tk()
    logo = PhotoImage(file='logo.png')
    a = Label(window, image=logo).grid(
        row=0, column=0, columnspan=2, sticky=N+E+S+W)
    window.title('Sudoku')
    window.geometry('400x400+300+300')
    text = Label(window, text='                          Select Difficulty ').grid(
        row=1, column=0)
    but_1 = Button(window, text="Easy", command=lambda window=window: set_difficulty(
        window, 5)).grid(row=3, column=0, columnspan=2, rowspan=2, sticky=N+S+E+W,)
    but_2 = Button(window, text="Hard", command=lambda window=window: set_difficulty(
        window, 4)).grid(row=5, column=0, columnspan=2, rowspan=2, sticky=N+E+S+W)
    but_3 = Button(window, text="Very Hard", command=lambda window=window: set_difficulty(
        window, 3)).grid(row=7, column=0, columnspan=2, rowspan=2, sticky=N+E+W+S)
    but_4 = Button(window, text="Insane", command=lambda window=window: set_difficulty(
        window, 2)).grid(row=9, column=0, columnspan=2, rowspan=2, sticky=N+E+S+W)
    window.mainloop()


difficulty_window()
makegame()


def mainwindow():
    start = time()
    window = Tk()
    window.title('Sudoku')
    window.geometry('400x400+300+300')
    tkinter.ttk.Separator(window, orient=VERTICAL).grid(
        row=0, column=3, rowspan=12, sticky='ns')
    tkinter.ttk.Separator(window, orient=VERTICAL).grid(
        row=0, column=7, rowspan=12, sticky='ns')
    tkinter.ttk.Separator(window, orient=VERTICAL).grid(
        row=0, column=11, rowspan=12, sticky='ns')
    tkinter.ttk.Separator(window, orient=HORIZONTAL).grid(
        row=3, column=0, columnspan=12, sticky='ew')
    tkinter.ttk.Separator(window, orient=HORIZONTAL).grid(
        row=7, column=0, columnspan=12, sticky='ew')
    tkinter.ttk.Separator(window, orient=HORIZONTAL,).grid(
        row=11, column=0, columnspan=12, sticky='ew')
    l = []
    d = {}
    for i in range(12):
        window.grid_columnconfigure(i, minsize=10, weight=1, pad=3)
        window.grid_rowconfigure(i, minsize=10, weight=1, pad=3)

    def isfilled():
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    return False
        return True

    def DisplayVictory():
        now = time()
        window = Tk()
        window.geometry('400x400+300+300')
        #congo = PhotoImage(file='congo.png')
        #a = Label(window,image=congo).pack()
        disp = "Congratulations!  YOU WON in - " + \
            str(round((start-now)/60, 2)) + "minutes"
        l = Label(window, text=disp).pack()
        window.mainloop()

    def callback(entryText, a, b):
        val = entryText.get()
        if val == '':
            sudoku[a][b] = 0
            d[(a, b)].configure(highlightbackground="white",
                                highlightcolor="white")  # empty cell

        elif val[0].isalpha() or len(val) > 1:  # invalid entry
            entryText.set("")

        elif val != str(s[a][b]):  # wrong entry
            d[(a, b)].configure(highlightbackground="red", highlightcolor="red")

        else:
            d[(a, b)].configure(highlightbackground="white", highlightcolor="white")
            sudoku[a][b] = int(entryText.get())

        if isfilled():
            window.destroy()
            DisplayVictory()

    for i in range(11):
        a = i
        if i > 7:
            a -= 2
        elif i > 3:
            a -= 1
        for j in range(11):
            b = j
            if j > 7:
                b = b-2
            elif j > 3:
                b = b-1
            if i == 3 or i == 7:
                i += 1
            if j == 3 or j == 7:
                j += 1
            label = (a, b)
            entryText = StringVar()
            d[label] = Entry(window, fg='green', width=2,
                             justify=CENTER, textvariable=entryText)
            d[label].grid(row=i, column=j, sticky=N+E+S+W, pady=1.5, padx=1.5)

            if sudoku[a][b] == 0:
                entryText.set("")
                entryText.trace("w", lambda name, index, mode,
                                entryText=entryText, a=a, b=b: callback(entryText, a, b))

            else:
                entryText.set(sudoku[a][b])
                d[label].config(state='disabled')
    window.mainloop()


mainwindow()

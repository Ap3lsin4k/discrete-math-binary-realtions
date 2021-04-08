from tkinter import Toplevel, Label, Listbox, EXTENDED, W, E, N, S, Button, GROOVE

from ui_stateful import UI


def initialize_ui():
    # Create Toplevel for window 2
    window3 = Toplevel()
    window3.title("Window 3")
    '''
       window2.maxsize(width=475,height=290)
       window2.minsize(width=475,height=290)
        '''
    # Labels
    lab1 = Label(window3, text='Set A', font='arial 20')
    lab2 = Label(window3, text='Set B', font='arial 20')
    # Listbox
    listbox1 = Listbox(window3, height=5, width=15, font=("Arial", 16), selectmode=EXTENDED)
    listbox2 = Listbox(window3, height=5, width=15, font=("Arial", 16), selectmode=EXTENDED)
    # Labels
    lab1.grid(row=1, column=1, sticky=W + E + N + S, pady=5, padx=5)
    lab2.grid(row=1, column=2, sticky=W + E + N + S, pady=5, padx=5)
    # Listbox
    listbox1.grid(row=2, column=1, sticky=W + E + N + S, pady=5, padx=5)
    listbox2.grid(row=2, column=2, sticky=W + E + N + S, pady=5, padx=5)
    return listbox1, listbox2, window3









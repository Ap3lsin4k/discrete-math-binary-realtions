from tkinter import Toplevel, Label, Listbox, EXTENDED, W, E, N, S, Button, GROOVE


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


def make_relation_button(window3, button_index, right_handed_people, left_handed_people, score, title):
    def build_and_show_relation_R():
        build_and_show_relation(right_handed_people, left_handed_people, score, title)

    but1 = Button(window3, text=title, command=build_and_show_relation_R, width=10, font=("Arial", 20))
    but1.grid(row=3, column=button_index, sticky=W + E + N + S, pady=5, padx=5)


def name_rows_or_cols(top, cells_info, row_range, column_range):
    for i in row_range:
        for j in column_range:
            lb = Label(top, text=cells_info[i + j + 1], font='arial 14')
            lb.grid(row=i + 1, column=j + 1)


def name_rows_and_cols(top, set_A, set_B):
    name_rows_or_cols(top, set_A, row_range=range(len(set_A)), column_range=(-1,))
    name_rows_or_cols(top, set_B, row_range=(-1,), column_range=range(len(set_B)))


def build_and_show_relation(set_A, set_B, score, title):
    top = initialize_relation_toplevel(title)
    name_rows_and_cols(top, set_A, set_B)
    fill_grid(score, set_A, set_B, top)


def fill_grid(score, set_A, set_B, top):
    calc = 0
    for r in range(1, len(set_A) + 1):
        for c in range(1, len(set_B) + 1):
            lb = Label(top, text=score[calc], font='arial 14')
            lb.grid(row=r, column=c)
            calc += 1


def initialize_relation_toplevel(title):
    top = Toplevel(height=500, width=100, relief=GROOVE)
    top.title(title)
    lab3 = Label(top, text=title, font='arial 14')
    lab3.grid(row=0, column=0)
    return top
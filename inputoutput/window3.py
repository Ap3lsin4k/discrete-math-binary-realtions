from tkinter import END

from inputoutput.repository import load_saved_sets
from inputoutput.ui import initialize_ui
from inputoutput.ui_window3 import UI

relation_S_plus_R = []


def create_window_3():

    listbox1, listbox2, window3 = initialize_ui()
    ppl = load_saved_sets()

    for i in ppl.A_names:
        listbox1.insert(END, i)
    for i in ppl.B_names:
        listbox2.insert(END, i)

    myui = UI(ppl)
    myui.initialize_and_save_husband_of_relation(window3)
    myui.initialize_and_save_father_in_law_of_relation(window3)





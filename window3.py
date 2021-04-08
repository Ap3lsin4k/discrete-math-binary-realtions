from tkinter import END

from repository import load_saved_sets
from ui import initialize_ui
from ui_stateful import UI
from user_story4 import compute_and_set_operations_on_relations

relation_S_plus_R = []

matrix = [["Relation S", "Олександр", "Віталій", "Богдан", "Сергій", "Микола", "Володимир", "Юрій", "Семен", "Зоя", "Аліна"],
          ["Катерина","0"],
          ["Адам",],
          ["Щек",],
        ["Ігор",],
        ["Віктор",],
        ["Гліб",],
    ["Данило",],
["Євген",],
  ["Дмитро",],
["Вадим",],
  ["Олег",],
  ["Михайло",],
  ["Людмила",],
]
def create_window_3():

    listbox1, listbox2, window3 = initialize_ui()
    ppl = load_saved_sets()

    for i in ppl.A:
        listbox1.insert(END, i)
    for i in ppl.B:
        listbox2.insert(END, i)

    myui = UI(ppl)
    myui.initialize_and_save_husband_of_relation(window3)

    myui.initialize_and_save_father_in_law_of_relation(window3)





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
    left_handed_people, right_handed_people = load_saved_sets()

    myui = UI(left_handed_people, right_handed_people)
    relation_S, score = myui.initialize_and_save_husband_of_relation(left_handed_people, right_handed_people, window3)

    relation_R = myui.initialize_and_save_father_in_law_of_relation(left_handed_people, right_handed_people, score, window3)

#    compute_and_set_operations_on_relations(left_handed_people, listbox1, listbox2, relation_R, relation_S,
 #                                           right_handed_people)
    from tkinter import END

    for i in right_handed_people:
        listbox1.insert(END, i)
    for i in left_handed_people:
        listbox2.insert(END, i)


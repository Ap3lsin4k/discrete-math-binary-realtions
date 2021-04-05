from tkinter import *
import random
import copy

relation_S_plus_R = []


# MATRIX builder
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



def create_window_3():
    list1 = ["Вікторія", "Світлана", "Марія", "Анна", "Дарина", "Катерина", "Людмила", "Зоя", "Аліна", "Олена", "Юлія",
             "Лариса", "Анастасія", "Антоніна", "Оксана", "Галина", "Тетяна", "Василина", "Валентина", "Інна"]
    # list2 = ["Андрій", "Петро", "Ігор", "Віктор", "Антон", "Євген", "Дмитро", "Вадим", "Олександр", "Віталій",
    # "Богдан", "Павел", "Сергій", "Микола", "Володимир", "Юрій", "Олег", "Михайло", "Семен", "Чіпка"]

    listbox1, listbox2, window3 = initialize_ui()
    left_handed_people, right_handed_people = load_saved_sets()

    ######################################RELATION S####################################################################

    relation_S = set_realtions_set_b_use(copy.copy(left_handed_people), right_handed_people, list1)
    score = get_score(right_handed_people, relation_S, left_handed_people)

    with open(r"Relation S.txt", "w", encoding="UTF-8") as f:
        for i in relation_S:
            f.write(str(i))

    make_relation_button(window3, 1, right_handed_people, left_handed_people, score, "Relation S")

    ######################################RELATION R####################################################################
    relation_R = []
    women_in_A = []
    women_in_B = []
    set_A_use1 = copy.copy(right_handed_people)
    set_B_use1 = copy.copy(left_handed_people)

    for i in set_A_use1:
        if i in list1:
            women_in_A.append(i)
    for j in set_B_use1:
        if j in list1:
            women_in_B.append(j)

    if len(women_in_A) >= len(women_in_B):
        for i in range(len(women_in_B)):
            sister1 = random.choice(women_in_B)
            sister2 = random.choice(women_in_A)
            p = (sister2, sister1)
            relation_R.append(p)
            del women_in_B[women_in_B.index(sister1)]
            del women_in_A[women_in_A.index(sister2)]
    else:
        for i in range(len(women_in_A)):
            sister1 = random.choice(women_in_B)
            sister2 = random.choice(women_in_A)
            p = (sister2, sister1)
            relation_R.append(p)
            del women_in_B[women_in_B.index(sister1)]
            del women_in_A[women_in_A.index(sister2)]

    with open(r"Relation R.txt", "w", encoding="UTF-8") as f:
        for i in relation_R:
            f.write(str(i) + " ")

    all2 = get_all_possible_relations(left_handed_people, right_handed_people)
    score1 = []
    for i in all2:
        if i in relation_R:
            score1.append(1)
        else:
            score1.append(0)

    make_relation_button(window3, 2, right_handed_people, left_handed_people, score, "Relation R")

    global relation_S_plus_R
    relation_S_plus_R = relation_S + relation_R
    global relation_S_on_R
    relation_S_on_R = []
    for i in relation_S:
        if i in relation_R:
            relation_S_on_R.append(i)

    global relation_R_diff_S
    relation_R_diff_S = []
    for i in relation_R:
        if i not in relation_S:
            relation_R_diff_S.append(i)

    global relation_U_diff_R
    relation_U_diff_R = []
    for i in get_all_possible_relations(right_handed_people, left_handed_people):
        if i not in relation_R:
            relation_U_diff_R.append(i)

    global s_tra
    s_tra = []
    s_tra = relation_S

    for i in right_handed_people:
        listbox1.insert(END, i)
    for i in left_handed_people:
        listbox2.insert(END, i)

def get_score(right_handed_people, relation_S, left_handed_people):
    score = []
    all1 = get_all_possible_relations(right_handed_people, left_handed_people)
    for i in all1:
        if i in relation_S:
            score.append(1)
        else:
            score.append(0)
    return score


def get_all_possible_relations(right_handed_people, left_handed_people):
    all1 = []
    for i in right_handed_people:
        for j in left_handed_people:
            p = i, j
            all1.append(p)
    return all1


def set_realtions_set_b_use(set_B_use, right_handed_people, list1):
    relation_S = []
    def set_relations():
        try:
            for right_handed in right_handed_people:
                if right_handed in list1:
                    deti = random.randint(1, 3)
                    for j in range(1, deti + 1):
                        child = random.choice(set_B_use)
                        if child not in list1:
                            del set_B_use[set_B_use.index(child)]
                            printer = right_handed, child

                            relation_S.append(printer)
                        else:
                            continue
                else:
                    continue
        except Exception as e:
            print(e)

    return relation_S


def load_saved_sets():
    f1 = open(r"Set A.txt", "r", encoding="UTF-8")
    right_handed_people = f1.read().split(" ")
    right_handed_people = right_handed_people[:-1]  # remove '' after split
    f2 = open(r"Set B.txt", "r", encoding="UTF-8")
    left_handed_people = f2.read().split(" ")
    left_handed_people = left_handed_people[:-1]
    return left_handed_people, right_handed_people


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

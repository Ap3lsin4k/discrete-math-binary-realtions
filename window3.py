from tkinter import *
from tkinter import messagebox
import random
import copy

relation_S_plus_R = []


def name_rows_or_cols(top, cells_info, row_length=1, column_length=1):
    for i in range(row_length):
        for j in range(column_length):
            lb = Label(top, text=cells_info[i + j], font='arial 14')
            lb.grid(row=i, column=j)


def create_window_3():
    # Create Toplevel for window 2
    window3 = Toplevel()
    window3.title("Window 3")
    '''
   window2.maxsize(width=475,height=290)
   window2.minsize(width=475,height=290)
    '''

    list1 = ["Вікторія", "Світлана", "Марія", "Анна", "Дарина", "Катерина", "Людмила", "Зоя", "Аліна", "Олена", "Юлія",
             "Лариса", "Анастасія", "Антоніна", "Оксана", "Галина", "Тетяна", "Василина", "Валентина", "Інна"]
    list2 = ["Андрій", "Петро", "Ігор", "Віктор", "Антон", "Євген", "Дмитро", "Вадим", "Олександр", "Віталій", "Богдан",
             "Павел", "Сергій", "Микола", "Володимир", "Юрій", "Олег", "Михайло", "Семен", "Чіпка"]

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

    f1 = open(r"Set A.txt", "r", encoding="UTF-8")
    set_A = f1.read().split(" ")
    set_A = set_A[:-1]  # remove '' after split
    f2 = open(r"Set B.txt", "r", encoding="UTF-8")
    set_B = f2.read().split(" ")
    set_B = set_B[:-1]

    ######################################RELATION S####################################################################
    set_B_use = copy.copy(set_B)
    relation_S = []
    try:
        for i in set_A:
            if i in list1:
                deti = random.randint(1, 3)
                for j in range(1, deti + 1):
                    child = random.choice(set_B_use)
                    if child not in list1:
                        del set_B_use[set_B_use.index(child)]
                        printer = i, child

                        relation_S.append(printer)
                    else:
                        continue
            else:
                continue
    except Exception as e:
        print(e)

    all1 = []
    for i in set_A:
        for j in set_B:
            p = i, j
            all1.append(p)
    topp = []
    for i in relation_S:
        topp.append(i[0])
    leftt = []
    for j in relation_S:
        leftt.append(j[1])
    score = []
    for i in all1:
        if i in relation_S:
            score.append(1)
        else:
            score.append(0)

    with open(r"Relation S.txt", "w", encoding="UTF-8") as f:
        for i in relation_S:
            f.write(str(i))

    def build_and_show_relation_S():
        top = Toplevel(height=500, width=100, relief=GROOVE)
        top.title("Relation S")
        calc = 0
        lab3 = Label(top, text="Relation S", font='arial 14')
        lab3.grid(row=0, column=0)

        name_rows_or_cols(top, set_A, row_length=(len(set_A)), column_length=1)
        name_rows_or_cols(top, set_B, row_length=1, column_length=len(set_B))

        for r in range(1, len(set_A) + 1):
            for c in range(1, len(set_B) + 1):
                lb = Label(top, text=score[calc], font='arial 14')
                lb.grid(row=r, column=c)
                calc += 1

    but1 = Button(window3, text="Relation S", command=build_and_show_relation_S, width=10, font=("Arial", 20))
    but1.grid(row=3, column=1, sticky=W + E + N + S, pady=5, padx=5)

    ######################################RELATION R####################################################################
    relation_R = []
    women_in_A = []
    women_in_B = []
    set_A_use1 = copy.copy(set_A)
    set_B_use1 = copy.copy(set_B)

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

    all2 = []
    for i in set_A:
        for j in set_B:
            p = i, j
            all2.append(p)
    score1 = []
    for i in all2:
        if i in relation_R:
            score1.append(1)
        else:
            score1.append(0)

    def build_and_show_realtion_R():
        top = Toplevel(height=500, width=100, relief=GROOVE)
        top.title("Relation R")
        calc = 0
        lab3 = Label(top, text="Relation R", font='arial 14')
        lab3.grid(row=0, column=0)


        name_rows_or_cols(top, set_A, row_length=len(set_A), column_length=1)
        name_rows_or_cols(top, set_B, row_length=1, column_length=len(set_B))

        for r in range(len(set_A)):
            for c in range(len(set_B)):
                lb = Label(top, text=score1[calc], font='arial 14')
                lb.grid(row=r + 1, column=c + 1)
                calc += 1

    but1 = Button(window3, text="Relation R", command=build_and_show_realtion_R, width=10, font=("Arial", 20))
    but1.grid(row=3, column=2, sticky=W + E + N + S, pady=5, padx=5)

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
    for i in all1:
        if i not in relation_R:
            relation_U_diff_R.append(i)

    global s_tra
    s_tra = []
    s_tra = relation_S

    for i in set_A:
        listbox1.insert(END, i)
    for i in set_B:
        listbox2.insert(END, i)

from tkinter import END

from business_logic import get_intersection, get_all_possible_relations


def compute_and_set_operations_on_relations(left_handed_people, listbox1, listbox2, relation_R, relation_S,
                                            right_handed_people):
    global relation_S_plus_R
    relation_S_plus_R = relation_S + relation_R
    global relation_S_on_R
    relation_S_on_R = []
    get_intersection(relation_S, relation_R)
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
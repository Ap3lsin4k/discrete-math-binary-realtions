from repository import load_saved_sets
from ui import initialize_ui
from user_story import initialize_and_save_father_in_law_of_relation, initialize_and_save_husband_of_relation
from user_story4 import compute_and_set_operations_on_relations

relation_S_plus_R = []


def create_window_3():

    listbox1, listbox2, window3 = initialize_ui()
    left_handed_people, right_handed_people = load_saved_sets()

    relation_S, score = initialize_and_save_husband_of_relation(left_handed_people, right_handed_people, window3)

    relation_R = initialize_and_save_father_in_law_of_relation(left_handed_people, right_handed_people, score, window3)

    compute_and_set_operations_on_relations(left_handed_people, listbox1, listbox2, relation_R, relation_S,
                                            right_handed_people)



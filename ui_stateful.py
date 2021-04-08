import copy
from tkinter import Toplevel, Label, W, E, N, S, Button, GROOVE

import binary_relation_generator
from business_logic import get_intersection, business_logic_generate_relation, set_realtions_set_b_use, get_score
from controller import cast_to_persons
from presenter import index_person_advanced, Presenter
from repository import save_relation_to_file
from user_story_stateful import UserStory


def initialize_toplevel(title):
    top = Toplevel(height=500, width=100, relief=GROOVE)
    top.title(title)

    return top


class UI:
    def __init__(self, left_handed_names, set_B_names):
        self.top = None
        self.fathers_in_law_indexes_on_grid = []
        self.sons_in_law_indexes_on_grid = []

        self.presenter = Presenter(left_handed_names, set_B_names)
        self.us = UserStory(relation_generator=binary_relation_generator,
                            one_set=cast_to_persons(left_handed_names),
                            another_set=cast_to_persons(set_B_names))
        self.us.generate_relations()

    def initialize_and_save_father_in_law_of_relation(self, left_handed_people, set_B_people, window3):
        from controller import women_names
        set_B_women = get_intersection(copy.copy(set_B_people), women_names)
        left_handed_women = get_intersection(left_handed_people, women_names)
        r = business_logic_generate_relation(left_handed_women, set_B_women)
        save_relation_to_file("Relation R", r)
        self.__make_relation_button(window3, 2, "Relation R")
        return r

    def initialize_and_save_husband_of_relation(self, window3):
        save_relation_to_file("Relation S", self.us.S_relations)
        self.__make_relation_button(window3, 1, "Relation S")
        return self.us.S_relations

    def __make_relation_button(self, window3, button_index, title):
        def __build_and_show_father_in_law_relation():
            if len(self.us.R_relations) == 0:
                raise ValueError
            self.__build_and_show_relation("father-in-law relation (Тесть)",
                                           self.us.R_relations, "Relation R")
            # TODO self.us.R_relations

        but1 = Button(window3, text=title, command=__build_and_show_father_in_law_relation, width=10, font=("Arial", 20))
        but1.grid(row=3, column=button_index, sticky=W + E + N + S, pady=5, padx=5)

    def __build_and_show_relation(self, title, relations, relation_table_name):
        self.top = initialize_toplevel(title)
        self.presenter.fill_cell_values(self, relations, relation_table_name)

    def show_values_in_grid(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.__fill_cell_at(matrix[i][j], i, j)

    def __fill_cell_at(self, text, row, column):
        lb = Label(self.top, text=text, font='arial 14')
        lb.grid(row=row, column=column)


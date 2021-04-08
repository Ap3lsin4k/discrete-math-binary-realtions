import copy
from tkinter import Toplevel, Label, W, E, N, S, Button, GROOVE

import binary_relation_generator
from business_logic import get_intersection, business_logic_generate_relation, set_realtions_set_b_use, get_score
from entity import Person
from presenter import index_person_advanced, convert_to_matrix, find_names_of_people_with_no_relation, Presenter
from repository import save_relation_to_file
from controller import cast_to_persons
from user_story_stateful import UserStory


def initialize_toplevel(title):
    top = Toplevel(height=500, width=100, relief=GROOVE)
    top.title(title)

    return top


class UI:
    def __init__(self, left_handed_names, right_handed_names):
        self.top = None
        self.fathers_in_law_indexes_on_grid = []
        self.sons_in_law_indexes_on_grid = []

        self.presenter = Presenter(left_handed_names, right_handed_names)
        self.us = UserStory(binary_relation_generator, cast_to_persons(right_handed_names),
                            cast_to_persons(left_handed_names))
        self.us.generate_relations()

    def make_relation_button(self, window3, button_index, title):
        def build_and_show_father_in_law_relation():
            if len(self.us.R_relations) == 0:
                raise ValueError
            self.build_and_show_relation("father-in-law relation (Тесть)",
                                         self.us.R_relations, "Relation R")

        but1 = Button(window3, text=title, command=build_and_show_father_in_law_relation, width=10, font=("Arial", 20))
        but1.grid(row=3, column=button_index, sticky=W + E + N + S, pady=5, padx=5)

    def build_and_show_relation(self, title, relations, relation_table_name):
        self.top = initialize_toplevel(title)
        self.presenter.fill_cell_values(self, relations, relation_table_name)

    def show_values_in_grid(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.fill_cell_at(matrix[i][j], i, j)

    def get_domain_index(self, person):
        return index_person_advanced(person, self.fathers_in_law_indexes_on_grid)

    def get_codomain_index(self, person):
        return index_person_advanced(person, self.sons_in_law_indexes_on_grid)

    def initialize_and_save_father_in_law_of_relation(self, left_handed_people, right_handed_people, score, window3):
        from controller import women_names
        right_handed_women = get_intersection(copy.copy(right_handed_people), women_names)
        left_handed_women = get_intersection(left_handed_people, women_names)
        r = business_logic_generate_relation(left_handed_women, right_handed_women)
        save_relation_to_file("Relation R", r)
        self.make_relation_button(window3, 2, "Relation R")
        return r

    def initialize_and_save_husband_of_relation(self, left_handed_people, right_handed_people, window3):
        from controller import women_names
        s = set_realtions_set_b_use(right_handed_people, copy.copy(left_handed_people), women_names)
        score = get_score(right_handed_people, s, left_handed_people)
        save_relation_to_file("Relation S", s)
        self.make_relation_button(window3, 1, "Relation S")
        return s, score

    def fill_cell_at(self, text, row, column):
        lb = Label(self.top, text=text, font='arial 14')
        lb.grid(row=row, column=column)

    def name_rows_and_columns(self, persons):
        for i in range(len(persons)):
            self.fill_cell_at(persons[i].name, i + 1, 0)

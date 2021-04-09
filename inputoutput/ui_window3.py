import pickle
from tkinter import Toplevel, Label, W, E, N, S, Button, GROOVE

from core import binary_relation_generator
from core.entity_two_groups import TwoGroupsOfPersons
from presentation.presenter import Presenter
from inputoutput.repository import save_relation_to_file
from core.user_story import UserStory


def initialize_toplevel(title):
    top = Toplevel(height=500, width=100, relief=GROOVE)
    top.title(title)

    return top


def make_relation_button(window3, button_index, title, command):
    but1 = Button(window3, text=title, command=command, width=10, font=("Arial", 20))
    but1.grid(row=3, column=button_index, sticky=W + E + N + S, pady=5, padx=5)


class UI:
    def __init__(self, people_names):
        self.top = None
        self.fathers_in_law_indexes_on_grid = []
        self.sons_in_law_indexes_on_grid = []

        self.presenter = Presenter(people_names)
        self.us = UserStory(relation_generator=binary_relation_generator,
                            people=people_names.cast_to_persons())
        self.us.generate_relations()
        all_people = TwoGroupsOfPersons(self.us.one_set, self.us.another_set, self.us.S_relations, self.us.R_relations)
        pickle.dump(all_people, open("../TwoGroups.pickle", "wb"))

    def initialize_and_save_father_in_law_of_relation(self, window3):
        self.initialize_relation(window3, 2, "Relation R", "father-in-law relation (Тесть)", self.us.R_relations)

    def initialize_and_save_husband_of_relation(self, window3):
        self.initialize_relation(window3, 1, "Relation S", "husband of relation (Чоловік)", self.us.S_relations)

    def initialize_relation(self, ui_root, button_index, short_title, long_title, relation):
        save_relation_to_file(short_title, relation)

        def build_and_show_relation():
            self.__build_and_show_relation(long_title, relation, short_title)

        make_relation_button(ui_root, button_index, short_title, build_and_show_relation)

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

from tkinter import Toplevel, GROOVE, Button, W, E, N, S, Label

from inputoutput.repository import save_relation_to_file


def initialize_toplevel(title):
    top = Toplevel(height=500, width=100, relief=GROOVE)
    top.title(title)
    return top


def make_button(window, row, column, command, title):
    but1 = Button(window, text=title, command=command, width=10, font=("Arial", 20))
    but1.grid(row=row, column=column, sticky=W + E + N + S, pady=5, padx=5)


class RelationsWindow:
    def __init__(self, presenter, user_story):
        super().__init__()
        self.presenter = presenter
        self.us = user_story
        #self.root = Toplevel()

    def initialize_relation(self, row, column, long_title, relation, short_title):
        save_relation_to_file(short_title, relation)

        def build_and_show_relation():
            self.__build_and_show_relation(long_title, relation, short_title)

        make_button(self.root_relation_controller, row, column, build_and_show_relation, short_title)

    def __build_and_show_relation(self, title, relations, relation_table_name):
        self.relation_top_level = initialize_toplevel(title)
        self.presenter.fill_cell_values(self, relations, relation_table_name)

    def show_values_in_grid(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.__fill_cell_at(matrix[i][j], i, j)

    def __fill_cell_at(self, text, row, column):
        lb = Label(self.relation_top_level, text=text, font='arial 14')
        lb.grid(row=row, column=column)

    def initialize(self, names): pass
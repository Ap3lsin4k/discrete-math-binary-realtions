from tkinter import Toplevel, Label, W, E, N, S, Listbox, EXTENDED, END

from inputoutput.relations_window import RelationsWindow, make_button


class WindowWithBasicRelations(RelationsWindow):

    def initialize(self, names):
        self.initialize_window3(names)
        self.presenter.initalize()
        self.initialize_and_save_husband_of_relation()
        self.initialize_and_save_father_in_law_of_relation()

    def initialize_and_save_father_in_law_of_relation(self):
        def build_and_show_relation():
            self.create_new_window(title)
            self.presenter.fill_cell_values(self, relations, relation_table_name)

        make_button(self.root_relation_controller, row, column, build_and_show_relation, short_title)

        self.initialize_relation()

    def initialize_and_save_husband_of_relation(self):
        self.initialize_relation(3, 1, "husband of relation (Чоловік)", self.us.S_relations, "Relation S")

    def initialize_window3(self, people):
        # Create Toplevel for window 2
        self.root_relation_controller = Toplevel()
        self.root_relation_controller.title("Window 3")
        '''
           window2.maxsize(width=475,height=290)
           window2.minsize(width=475,height=290)
            '''
        # Labels
        lab1 = Label(self.root_relation_controller, text='Set A', font='arial 20')
        lab2 = Label(self.root_relation_controller, text='Set B', font='arial 20')
        # Listbox
        listbox1 = Listbox(self.root_relation_controller, height=5, width=15, font=("Arial", 16), selectmode=EXTENDED)
        listbox2 = Listbox(self.root_relation_controller, height=5, width=15, font=("Arial", 16), selectmode=EXTENDED)
        # Labels
        lab1.grid(row=1, column=1, sticky=W + E + N + S, pady=5, padx=5)
        lab2.grid(row=1, column=2, sticky=W + E + N + S, pady=5, padx=5)
        # Listbox
        listbox1.grid(row=2, column=1, sticky=W + E + N + S, pady=5, padx=5)
        listbox2.grid(row=2, column=2, sticky=W + E + N + S, pady=5, padx=5)

        for i in people.A_names:
            listbox1.insert(END, i)
        for i in people.B_names:
            listbox2.insert(END, i)

        return self.root_relation_controller

    def make_button(self, row, column, build_and_show_relation, short_title):
        make_button(self.root_relation_controller, row, column, build_and_show_relation, short_title)

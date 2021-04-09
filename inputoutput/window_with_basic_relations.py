from tkinter import Toplevel, Label, W, E, N, S, Listbox, EXTENDED, END

from inputoutput.relations_window import RelationsWindow


class WindowWithBasicRelations(RelationsWindow):

    def initialize(self, names):
        self.initialize_window3(names)
        self.initialize_and_save_husband_of_relation()
        self.initialize_and_save_father_in_law_of_relation()

    def initialize_and_save_father_in_law_of_relation(self):
        self.initialize_relation(3, 2, "father-in-law relation (Тесть)", self.us.R_relations, "Relation R")

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

from tkinter import Toplevel, Label, GROOVE

from inputoutput.relations_window import RelationsWindow


class WindowWithComplexRelations(RelationsWindow):

    def initialize_window4(self, people):
        top = Toplevel(height=500, width=100, relief=GROOVE)
        top.title("U \ R")
        lab3 = Label(top, text="U \ R", font='arial 14')
        lab3.grid(row=0, column=0)
        self.root_relation_controller = top

    def initialize_and_save_U_diff_R(self):
        self.initialize_relation(1, 1, "U \ R", self.us.U_diff_R(), "U \ R")


    def initialize_U_diff_R(self):
        # Controller
        self.us.U_diff_R()
        self.initialize_relation(1, 1, "U difference R", groups.R_complement(), "U \ R")


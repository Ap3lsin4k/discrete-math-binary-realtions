from tkinter import Toplevel, Label, GROOVE

from inputoutput.relations_window import RelationsWindow


class WindowWithComplexRelations(RelationsWindow):

    def initialize_window4(self):
        window4 = Toplevel()
        window4.title("Window 4")
        self.root_relation_controller = window4


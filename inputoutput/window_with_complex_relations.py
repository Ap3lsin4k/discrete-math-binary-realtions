from tkinter import Toplevel, Label, GROOVE

from inputoutput.relations_window import RelationsWindow


class WindowWithComplexRelations(RelationsWindow):

    def initialize_window4(self):
        window4 = Toplevel()
        window4.title("Window 4")
#        window4.maxsize(width=475,height=290)
 #       window4.minsize(width=475,height=290)
        self.root_relation_controller = window4


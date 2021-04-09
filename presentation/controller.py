from core.entity import Person




class Controller():
    def __init__(self, us):
        self.us = us
    def initialize_U_diff_R(self):
        # Controller
        self.us.U_diff_R()
        self.initialize_relation(1, 1, "U difference R", groups.R_complement(), "U \ R")
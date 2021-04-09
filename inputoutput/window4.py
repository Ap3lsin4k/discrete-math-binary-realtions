import pickle
from tkinter import *
from tkinter import messagebox
import random
import copy
import deprecated_operations_on_binary_relations_controller
from core import binary_relation_generator
from core.user_story import UserStory
from inputoutput.window_with_complex_relations import WindowWithComplexRelations
from presentation.presenter import Presenter


def create_window_4():

   #Create Toplevel for window 2
   window4 = Toplevel()
   window4.title("Window 4")
   #window2.maxsize(width=475,height=290)
   #window2.minsize(width=475,height=290)

   groups = pickle.load(open("../TwoGroups.pickle", "rb"))

   ui = WindowWithComplexRelations(presenter=None,
                                   user_story=None)
   presenter = Presenter(groups.cast_to_names(), ui)
   us = UserStory(binary_relation_generator, groups, presenter=presenter)
   controller = ui
   controller.us = us


   ui.initialize_window4(None)
   #########################FUNCTIONS####################################
   but1 = Button(window4, text="R ∪ S ", command=deprecated_operations_on_binary_relations_controller.R_or_S, width=10, font=("Arial", 20))
   but2 = Button(window4, text="R ∩ S", command=deprecated_operations_on_binary_relations_controller.R_and_S, width=10, font=("Arial", 20))
   but3 = Button(window4, text="R \ S", command=deprecated_operations_on_binary_relations_controller.R_diff_S, width=10, font=("Arial", 20))

   controller.initialize_window4(None)
   controller.initialize_and_save_U_diff_R()
   #make_button(window4, 1, 1, _, "U \ R")
   but4 = Button(window4, text="U \ R", command=deprecated_operations_on_binary_relations_controller.U_diff_R, width=10, font=("Arial", 20))
   but4.grid(row=1, column=1, sticky=W+E+N+S, pady=5, padx=5)

   but5 = Button(window4, text="s^(-1)", command=deprecated_operations_on_binary_relations_controller.S_tra, width=10, font=("Arial", 20))


   but1.grid(row=0, column=0, sticky=W+E+N+S, pady=5, padx=5)
   but2.grid(row=0, column=1, sticky=W+E+N+S, pady=5, padx=5)
   but3.grid(row=1, column=0, sticky=W+E+N+S, pady=5, padx=5)
   but5.grid(row=2, column=0,columnspan=2, sticky=W+E+N+S, pady=5, padx=5)

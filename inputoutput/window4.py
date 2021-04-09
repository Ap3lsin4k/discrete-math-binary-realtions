import pickle
from tkinter import *
from tkinter import messagebox
import random
import copy
import deprecated_operations_on_binary_relations_controller
from core import binary_relation_generator
from core.complex_user_story import ComplexUserStory
from core.user_story import UserStory
from inputoutput.window_with_complex_relations import WindowWithComplexRelations
from presentation.complex_presenter import ComplexPresenter
from presentation.presenter import Presenter


def create_window_4():

   groups = pickle.load(open("../TwoGroups.pickle", "rb"))

   ui = WindowWithComplexRelations(presenter=None,
                                   user_story=None)
   presenter = ComplexPresenter(groups.cast_to_names(), ui)
   us = ComplexUserStory(binary_relation_generator, groups, presenter=presenter)

   ui.initialize_window4()

   us.execute()
   controller = ui
   controller.us = us


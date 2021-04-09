import pickle
from tkinter import END

from core import binary_relation_generator
from core.entity_two_groups import TwoGroupsOfPersons
from core.user_story import UserStory
from inputoutput.repository import load_names_for_two_groups
from inputoutput.ui_window3 import WindowWithBasicRelations
from presentation.presenter import Presenter

relation_S_plus_R = []


def create_window_3_facade():

    names = load_names_for_two_groups()

    presenter = Presenter(names)
    us = UserStory(relation_generator=binary_relation_generator,
                        people=names.cast_to_persons())
    us.generate_relations()
    pickle_dump(us)
    myui = WindowWithBasicRelations(presenter, user_story=us)
    myui.initialize(names)


def pickle_dump(us):
    all_people = TwoGroupsOfPersons(us.one_set, us.another_set, us.S_relations, us.R_relations)
    pickle.dump(all_people, open("../TwoGroups.pickle", "wb"))





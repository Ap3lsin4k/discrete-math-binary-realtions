import pickle
from tkinter import END

from core import binary_relation_generator
from core.basic_user_story import BasicUserStory
from core.entity_two_groups import TwoGroupsOfPersons
from core.user_story import UserStory
from inputoutput.repository import load_names_for_two_groups
from inputoutput.window_with_basic_relations import WindowWithBasicRelations
from presentation.presenter import Presenter, BasicPresenter

relation_S_plus_R = []


def create_window_3_facade():

    names = load_names_for_two_groups()

    myui = WindowWithBasicRelations(None, None)
    myui.initialize_window3(names)

    presenter = BasicPresenter(names, myui)
    us = BasicUserStory(relation_generator=binary_relation_generator,
                        people=names.cast_to_persons(), presenter=presenter)
    us.generate_relations()
    us.execute()


    pickle_dump(us)


def pickle_dump(us):
    all_people = TwoGroupsOfPersons(us.one_set, us.another_set, us.S_relations, us.R_relations)
    pickle.dump(all_people, open("../TwoGroups.pickle", "wb"))





import pickle

from core import complex_user_story, binary_relation_generator
from core.complex_user_story import ComplexUserStory
from inputoutput.window_with_complex_relations import WindowWithComplexRelations


def test_complex():
    groups = pickle.load(open("../TwoGroups.pickle", "rb"))
    ui = WindowWithComplexRelations(presenter=None,
                                    user_story=None)
    us = ComplexUserStory(None, groups, presenter=None)


    assert us.union()
    assert us.inverse_of_S()
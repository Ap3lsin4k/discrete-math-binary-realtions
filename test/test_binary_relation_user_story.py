import binary_relation_generator
from entity_two_groups import TwoGroups
from user_story_stateful import UserStory


def test_user_story():
    us = UserStory(binary_relation_generator, TwoGroups(set(), set()))
    us.generate_relations()
    assert us.S_relations is not None
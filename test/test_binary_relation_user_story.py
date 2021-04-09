from core import binary_relation_generator
from core.entity_two_groups import TwoGroups
from core.user_story import UserStory


def test_user_story():
    us = UserStory(binary_relation_generator, TwoGroups(set(), set()).cast_to_persons())
    us.generate_relations()
    assert us.S_relations is not None

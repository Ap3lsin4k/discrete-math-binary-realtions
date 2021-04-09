from core.entity_two_groups import *


def test_two_group_complement(male, male1, male2, male3, female, female1, female2, female3):
    groups = TwoGroupsAndTwoRelations({male}, {male2, female3},
                                      {(None, None)}, {(male, male2)})
    assert groups.R_complement() == {(male, female3)}


def test_R_complement2(male, male1, male2, male3, female, female1, female2, female3):
    groups = TwoGroupsAndTwoRelations({male, male1, female, female1}, {male2, female2},
                                      {(male, None)}, {(male, male2), (female, male2), (female1, male2)})
    assert len(groups.R_complement()) == 5

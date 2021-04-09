from core.entity import Person


# noinspection PyPep8Naming
def test_S_relations(female, female2, male):
    impossible_husband = female
    wife = female2
    assert not impossible_husband.can_be_husband_of(wife)
    husband = male
    assert not husband.can_be_husband_of(husband)


# noinspection PyPep8Naming
def test_incorrect_R_relations(dummy):
    impossible_father_in_law = Person(sex="female")
    assert not impossible_father_in_law.can_be_father_in_law_of(dummy)
    father_in_law = Person(sex="male")
    impossible_son_in_law = Person(sex="female")
    assert not father_in_law.can_be_father_in_law_of(impossible_son_in_law)
    assert not father_in_law.can_be_father_in_law_of(father_in_law)


# noinspection PyPep8Naming
def test_correct_R_relations():
    father_in_law = Person(sex="male")
    son_in_law = Person(sex="male")
    assert father_in_law.can_be_father_in_law_of(son_in_law)
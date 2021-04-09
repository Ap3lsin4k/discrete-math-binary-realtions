from presentation.presenter import find_names_of_people_with_no_relation


def test_find_people_from_set_with_no_relation(male, male1, male2, male3, female):
    assert find_names_of_people_with_no_relation({male.name, male1.name}, {(male, male2)}) == {male1.name}



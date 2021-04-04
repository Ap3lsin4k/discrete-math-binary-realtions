from binary_relation_generator import generate_father_in_law_relations
from test.pytest_common_fixtures import *


def test_generated_relation_is_valid_and_test_clojure(right_handed, left_handed):
#    S = husband_of = {(male, female), ("Petro", "Nadia")}
#    R = father_in_law_of = {("")}

    valid_relations = generate_father_in_law_relations(right_handed, left_handed)
    for r in valid_relations:
        assert r[0].can_be_father_in_law_of(r[1])
    assert len(valid_relations) == 1


def test_does_not_generate_invalid_relation(male, female):
    relations = generate_father_in_law_relations(male, female, R_relations=set())
    assert len(relations) == 0

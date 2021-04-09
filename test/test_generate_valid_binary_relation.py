from core.binary_relation_generator import *


def test_generated_relation_is_valid_and_test_clojure(set_B, left_handed):
#    S = husband_of = {(male, female), ("Petro", "Nadia")}
#    R = father_in_law_of = {("")}
    valid_relations = set()
    set_B.generate_father_in_law_relation(left_handed, valid_relations)

    assert len(valid_relations) == 1
    binary_relation = valid_relations.pop()

    assert binary_relation[0].can_be_father_in_law_of(binary_relation[1])
    assert len(binary_relation) == 2


def test_does_not_generate_invalid_relation(male, female):
    relations = set()
    male.generate_father_in_law_relation(female, out_relation=relations)
    assert len(relations) == 0

    male.generate_father_in_law_relation(male, relations)
    assert len(relations) == 0


def test_generate_multiple_relations(male, male1, male2, male3, female, female1, female2, female3):
    rels = generate_random_father_in_law_relations_from_sets({male, male1, male2}, {male, female, male3})
    assert rels is not None
    assert len(rels) == 1 or len(rels) == 2


def test_generate_husband_relations(male, male1, male2, male3, female, female1, female2, female3):
    rels = generate_husband_relations_from_sets({male, male1, male2}, {male, female, male3})
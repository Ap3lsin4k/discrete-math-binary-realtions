import random


def _():
    G = 4
    N = 23
    M = "ІО"
    print("Моя група: ", M + "-", G)
    print("Мій номер у групі:", N)
    if M == "ІО": N += 1
    print("Мій варіант:", (N + G % 60) % 30 + 1)


def generate_random_father_in_law_relations_from_sets(set_A, set_B):
    R_relations = set()

    for right_handed in set_B:
        left_handed = random.choice(list(set_A))
        left_handed.generate_father_in_law_relation(right_handed, R_relations)

    return R_relations


def generate_all_possible_relations(set_A, set_B):
    U_relations = set()
    for left_handed in set_A:
        for right_handed in set_B:
            left_handed.force_generate_relation(right_handed, U_relations)

    return U_relations


def generate_husband_relations_from_sets(righthanders, lefthanders):
    R_relations = set()
    for a in righthanders:
        for left_handed in lefthanders:
            a.generate_husband_relation(left_handed, R_relations)

    return R_relations

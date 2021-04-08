import random


def _():
    G = 4
    N = 23
    M = "ІО"
    print("Моя група: ", M + "-", G)
    print("Мій номер у групі:", N)
    if M == "ІО": N += 1
    print("Мій варіант:", (N + G % 60) % 30 + 1)


def generate_father_in_law_relations_from_sets(righthanders, lefthanders):
    R_relations = set()

    for left_handed in lefthanders:
        right_handed = random.choice(list(righthanders))
        right_handed.generate_father_in_law_relation(left_handed, R_relations)

    return R_relations


def generate_husband_relations_from_sets(righthanders, lefthanders):
    R_relations = set()
    for right_handed in righthanders:
        for left_handed in lefthanders:
            right_handed.generate_husband_relation(left_handed, R_relations)

    return R_relations
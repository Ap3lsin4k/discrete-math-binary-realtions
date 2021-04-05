def _():
    G = 4
    N = 23
    M = "ІО"
    print("Моя група: ", M + "-", G)
    print("Мій номер у групі:", N)
    if M == "ІО": N += 1
    print("Мій варіант:", (N + G % 60) % 30 + 1)


class Person:
    sex: str

    def __init__(self, sex="female"):
        self.sex = sex
        self.bachelor = True

    def do_job_based_on_sex(self, job_for_males, job_for_females):
        if self.sex == "male":
            job_for_males()
        elif self.sex == "female":
            job_for_females()
        else:
            raise ValueError("Check the spelling for sex property.")

    # one to many
    def can_be_father_in_law_of(father_in_law, son_in_law):
        return father_in_law.sex == "male" and son_in_law.sex == "male" \
               and father_in_law is not son_in_law

    # one to one
    def can_be_husband_of(husband, wife):
        return husband.sex == "male" and wife.sex == "female" \
                and husband.bachelor and wife.bachelor

    def generate_father_in_law_relation(self, other, out_relation):
        if self.can_be_father_in_law_of(other):
            out_relation.add((self, other))

    def generate_husband_relation(self, possible_wife, out_relation):
        if self.can_be_husband_of(possible_wife):
            out_relation.add((self, possible_wife))
            self.bachelor = False
            possible_wife.bachelor = False


def generate_father_in_law_relations_from_sets(righthanders, lefthanders):
    R_relations = set()
    for right_handed in righthanders:
        for left_handed in lefthanders:
            right_handed.generate_father_in_law_relation(left_handed, R_relations)

    return R_relations


def generate_husband_relations_from_sets(righthanders, lefthanders):
    R_relations = set()
    for right_handed in righthanders:
        for left_handed in lefthanders:
            right_handed.generate_husband_relation(left_handed, R_relations)

    return R_relations
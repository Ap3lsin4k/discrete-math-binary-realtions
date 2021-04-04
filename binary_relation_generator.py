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

    def do_job_based_on_sex(self, job_for_males, job_for_females):
        if self.sex == "male":
            job_for_males()
        elif self.sex == "female":
            job_for_females()
        else:
            raise ValueError("Check the spelling for sex property.")

    def can_be_father_in_law_of(father_in_law, son_in_law):
        return father_in_law.sex == "male" and son_in_law.sex == "male" \
               and father_in_law is not son_in_law

    def can_be_husband_of(husband, wife):
        return husband.sex == "male" and wife.sex == "female"


# noinspection PyDefaultArgument
def generate_father_in_law_relations(right_handed_pers, left_handed_pers, R_relations=set()):
    if right_handed_pers.can_be_father_in_law_of(left_handed_pers):
        R_relations.add((right_handed_pers, left_handed_pers))
    return R_relations


def generate_relation(a, relation_rule, b, accumulative_relations=set()):
    if a.relation_rule(b):
        accumulative_relations.add((a, b))
    return accumulative_relations


def generate_father_in_law_relations_from_sets(righthanders, lefthanders):
    right_handed_pers = righthanders.pop()
    left_handed_pers = lefthanders.pop()
    # noinspection PyPep8Naming
    R_relations = set()
    if right_handed_pers.can_be_father_in_law_of(left_handed_pers):
        R_relations.add((right_handed_pers, left_handed_pers))
    return R_relations

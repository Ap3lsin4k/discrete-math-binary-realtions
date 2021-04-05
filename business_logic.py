import random


def business_logic_generate_relation(left_handed_women, right_handed_women):
    relation_R = []
    num_of_relations = min(len(right_handed_women), len(left_handed_women))
    for i in range(num_of_relations):
        sister1 = random.choice(left_handed_women)
        sister2 = random.choice(right_handed_women)
        p = (sister2, sister1)
        relation_R.append(p)
        del left_handed_women[left_handed_women.index(sister1)]
        del right_handed_women[right_handed_women.index(sister2)]
    return relation_R


def set_realtions_set_b_use(right_handed_people, set_B_use, list1):
    relation_S = []

    try:
        for right_handed in right_handed_people:
            if right_handed in list1:
                deti = random.randint(1, 3)
                for j in range(1, deti + 1):
                    child = random.choice(set_B_use)
                    if child not in list1:
                        del set_B_use[set_B_use.index(child)]
                        printer = right_handed, child

                        relation_S.append(printer)
                    else:
                        continue
            else:
                continue
    except Exception as e:
        print(e)
    return relation_S


def get_intersection(A, B):
    intersection = []
    for i in A:
        if i in B:
            intersection.append(i)
    return intersection


def get_score(right_handed_people, relation_S, left_handed_people):
    score = []
    all1 = get_all_possible_relations(right_handed_people, left_handed_people)
    for i in all1:
        if i in relation_S:
            score.append(1)
        else:
            score.append(0)
    return score


def get_all_possible_relations(right_handed_people, left_handed_people):
    all1 = []
    for i in right_handed_people:
        for j in left_handed_people:
            p = i, j
            all1.append(p)
    return all1
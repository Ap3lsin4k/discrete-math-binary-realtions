from entity_two_groups import TwoGroups


def load_saved_sets():
    f1 = open(r"Set A.txt", "r", encoding="UTF-8")
    set_A_names = f1.read().split(" ")
    set_A_names = set_A_names[:-1]  # remove '' after split
    f2 = open(r"Set B.txt", "r", encoding="UTF-8")
    set_B_people = f2.read().split(" ")
    set_B_people = set_B_people[:-1]

    return TwoGroups(set_A_names, set_B_people)


def save_relation_to_file(name, relation_itself):
    with open(str(name)+".txt", "w", encoding="UTF-8") as f:
        for i in relation_itself:
            f.write(str(i))
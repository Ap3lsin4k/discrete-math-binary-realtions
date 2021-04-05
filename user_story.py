import copy

from business_logic import get_intersection, business_logic_generate_relation, set_realtions_set_b_use, get_score
from repository import save_relation_to_file
from ui import make_relation_button

women_names = ["Вікторія", "Світлана", "Марія", "Анна", "Дарина", "Катерина", "Людмила", "Зоя", "Аліна", "Олена",
               "Юлія",
               "Лариса", "Анастасія", "Антоніна", "Оксана", "Галина", "Тетяна", "Василина", "Валентина", "Інна"]

def initialize_and_save_father_in_law_of_relation(left_handed_people, right_handed_people, score, window3):
    right_handed_women = get_intersection(copy.copy(right_handed_people), women_names)
    left_handed_women = get_intersection(left_handed_people, women_names)
    relation_R = business_logic_generate_relation(left_handed_women, right_handed_women)
    save_relation_to_file("Relation R", relation_R)
    make_relation_button(window3, 2, right_handed_people, left_handed_people, score, "Relation R")
    return relation_R


def initialize_and_save_husband_of_relation(left_handed_people, right_handed_people, window3):
    relation_S = set_realtions_set_b_use(right_handed_people, copy.copy(left_handed_people), women_names)
    score = get_score(right_handed_people, relation_S, left_handed_people)
    save_relation_to_file("Relation S", relation_S)
    make_relation_button(window3, 1, right_handed_people, left_handed_people, score, "Relation S")
    return relation_S, score
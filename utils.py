import json
from Class_Candidates import Candidates


def load_candidates(path):
    """
    Функция загружает данные из файла
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_all(data):
    """
    Функция показывает всех кандидатов
    """
    candidates_list = []
    for item in data:
        candidate = Candidates(item['pk'], item['name'], item['picture'], item['position'], item['skills'])
        candidates_list.append(candidate)
    return candidates_list


def get_by_pk(pk, candidates_list):
    """
    Функция возвращает кандидата по pk
    """
    for item in candidates_list:
        if item.pk == pk:
            return item


def get_by_skill(skill, candidates_list):
    """
    Функция возвращает кандидатов по навыку
    """
    skill_names = []
    for item in candidates_list:
        if skill.lower() in item.skills.lower():
            skill_names.append(item)
    return skill_names

import json

from config import DATA_PATH


def _load_data(path=DATA_PATH):
    """
    Загружает данные про кандидатов
    """
    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    return data


def load_candidates_from_json():
    """
    Возвращает список всех кандидатов
    """
    data = _load_data()

    return data


def get_candidate(pk):
    """
    Возвращает одного кандидата по его id
    """
    candidates = _load_data()
    for candidate in candidates:
        if candidate["id"] == pk:

            return candidate


def get_candidates_by_name(candidate_name):
    """
    Возвращает кандидатов по имени
    """
    candidates_names = []
    candidate_name_lower = candidate_name.lower()
    counter = 0

    candidates = _load_data()
    for candidate in candidates:
        candidate_name = candidate["name"].strip().lower()
        if candidate_name[0] in candidate_name_lower:
            candidates_names.append(candidate)
            counter += 1
            continue

    return candidates_names


def get_candidates_by_skill(skill_name):
    """
    Возвращает кандидатов по навыку
    """
    skilled_candidates = []
    skill_name_lower = skill_name.lower()
    counter = 0

    candidates = _load_data()
    for candidate in candidates:
        skills = candidate["skills"].lower().strip().split(", ")
        if skill_name_lower in skills:
            skilled_candidates.append(candidate)
            counter += 1
            continue

    return skilled_candidates

#!/usr/bin/python3
<<<<<<< HEAD
# 10-best_score.py
# Toriola Samuel


def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    ret = list(a_dictionary.keys())[0]
    big = a_dictionary[ret]
    for k, v in a_dictionary.items():
        if v > big:
            big = v
            ret = k
    return (ret)
=======
def best_score(a_dictionary):
    if a_dictionary is not None:
        students_number = len(a_dictionary.values())
        if students_number > 0:
            score = max(a_dictionary.values())
            for key in a_dictionary.keys():
                if a_dictionary[key] == score:
                    return key
    return None
>>>>>>> 6a930072f1b2ea8f27ef8504aaaaaf6ffe9037c8

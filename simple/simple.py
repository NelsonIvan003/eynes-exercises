import random


def simple_list():
    list_dict = []
    for id in range(1, 11):
        data_dict = {"id": id, "age": random.randint(1, 100)}
        list_dict.append(data_dict)
    print(list_dict)
    return list_dict


def sort_list(l_dict):
    sorted_list = sorted(l_dict, key=lambda a: a["age"])
    return sorted_list

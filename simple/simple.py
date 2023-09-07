import random


def simple_list():
    list_dict = []
    for id in range(1, 11):
        data_dict = {"id": id, "age": random.randint(1, 100)}
        list_dict.append(data_dict)

    print(list_dict)
    return list_dict


def sort_list(l_dict=None):
    sorted_list = sorted(l_dict, key=lambda a: a["age"])
    print(sorted_list)
    return sorted_list
    pass


#sort_list(simple_list())
sort_list([{'id': 1, 'age': 52}, {'id': 2, 'age': 77}, {'id': 3, 'age': 52}, {'id': 4, 'age': 52}, {'id': 5, 'age': 93}, {'id': 6, 'age': 13}, {'id': 7, 'age': 34}, {'id': 8, 'age': 52}, {'id': 9, 'age': 12}, {'id': 10, 'age': 52}])



import random


def simple_list():
    list_dict = []
    for id in range(1, 11):
        data_dict = {"id": id, "age": random.randint(1, 100)}
        list_dict.append(data_dict)

    print(list_dict)
    return list_dict


def sort_list(l_dict=None):
    print("Retornar la lista ordenada por edades --> # lo que podría agregar es que si hay dos edades iguales entonces"
          "se mostrará primero el menor id")
    pass


simple_list()
sort_list()

import functools as ft

""" method 1"""


def method1(lst):
    flat_list = []
    for sublist in lst:
        flat_list.extend(sublist)


""" method 2"""


def method2(lst):
    newList = ft.reduce(lambda x, y: x + y, lst)

    return newList


""" method 3"""


def method3(lst):
    flat_list = []

    for i in lst:

        for j in i:
            flat_list.append(j)

    return flat_list


l = [[1, 2, 3, 4], [4, 6], [8, 9], [10, 2]]

print(method3(l))

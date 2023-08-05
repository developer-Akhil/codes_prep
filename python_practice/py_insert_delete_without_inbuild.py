""" Q Write a python script to insert and delete the element from a list without using insert and pop function? """


def insert_fun(lst, idx, insert_val):
    newList = lst[:idx] + [insert_val] + lst[idx:]

    return newList


def delete_fun(lst, delete_val):
    newList = []
    for i in lst:

        if i != delete_val:
            newList.append(i)
    return newList


lst = [1, 2, 3, 6, 7, 8, 9]
a = 4
idx = 3
print(insert_fun(lst, idx, a))

print(delete_fun(lst, 6))

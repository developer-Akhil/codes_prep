input_val = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]

new_lst = []


def append_val(lst):
    for i in lst:

        if type(i) is list:
            append_val(i)
        else:
            new_lst.append(i)

    return new_lst


print(append_val(input_val))

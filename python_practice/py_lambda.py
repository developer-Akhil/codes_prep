from functools import reduce

new_list = [57, 22, 97, 54, 62, 77]

""" map """

# finalList = list(map(lambda x: x * 2, new_list))
#
# print(finalList)

""" filter """

# finalList = list(filter(lambda x :  (x%2 != 0), new_list))
#
# print(finalList)

""" reducer """

redc = reduce(lambda a, b: a + b, new_list)

print(redc)

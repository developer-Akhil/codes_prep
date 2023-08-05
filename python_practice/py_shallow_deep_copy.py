""" Normal Copy """
# numbers = [1, 2, 3, 4, 5]
#
# new_numbers = numbers
#
# new_numbers[0] = 9
#
# print('Number list', numbers)
# print('ID of number:', id(numbers))
#
# print('Number list', new_numbers)
# print('ID of number:', id(new_numbers))

""" Shallow Copy """
import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_list = copy.copy(old_list)

new_list[0] = ['a', 'b', 'c']

# new_list[0][2] = 'c'

print("Old list:", old_list)
print("Old list:", id(old_list))

print("new list:", new_list)
print("new list:", id(new_list))

""" Deep Copy """

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_list = copy.deepcopy(old_list)

new_list[0] = ['a', 'b', 'c']

# new_list[0][2] = 'c'

print("Old list:", old_list)
print("id for Old list:", id(old_list))

print("new list:", new_list)
print("id for new list:", id(new_list))


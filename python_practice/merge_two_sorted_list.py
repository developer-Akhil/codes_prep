list1 = [1, 3, 5, 8]
list2 = [2, 4, 6, 7,9]

# Using stack
sorted_list = []
while list1 and list2:
    if list1[0] < list2[0]:
        sorted_list.append(list1.pop(0))
    else:
        sorted_list.append(list2.pop(0))

print(list2)
print(list1)
sorted_list += list1
sorted_list += list2
print(sorted_list)

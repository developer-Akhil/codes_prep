listName = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, 30):
    listName.insert(0, listName.pop())

print(listName)

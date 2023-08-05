result = []

a = [1, 2, 3, 4, 5]


for first, second in zip(a, a[1:]):
    print(first, second)

for i in range(len(a) - 1):
    val = a[i:i + 2]

    result.append(val)

print(result)

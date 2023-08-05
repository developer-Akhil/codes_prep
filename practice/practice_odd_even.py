

def evenOdd(nums):

    evens = []
    odds = []
    for num in range(1, nums + 1):

        if num % 2 == 0:

            evens.append(num)

        else:
            odds.append(num)


    print(evens)
    print(odds)

print(evenOdd(10))
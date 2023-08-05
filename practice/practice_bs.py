
def binary_search(lst,n):

    first = 0
    last = len(lst) - 1

    while first <= last:

        mid = (first + last) // 2

        if lst[mid] == n:

            return "The location of values is {}".format(mid + 1)

        elif lst[mid] > n:

            last = mid - 1

        else:

            first = mid + 1

    if first > last:

        return "there is no value exist "

print(binary_search([1,2,3,4,5,6,7,8,10],6))
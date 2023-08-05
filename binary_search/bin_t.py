# PWC

# O(n/2)
# def bin_s_t(list_1, n):
#     low = 0
#     high = len(list_1) - 1
#
#     mid = 0
#
#     while low <= high:  # 0<=5
#         mid = (high + low) // 2  # mid 5+0//2 =2 | 5+3//2 = 4 |  5 + 5 //2 =5
#
#         if list_1[mid] < n:  # list_1[2] = 12, 12<39 , low=3 , 39 < 39 | list_1[4] =32  < 39 low= 4+1 =5 | 39 < 39
#             low = mid + 1
#         elif list_1[mid] > n:
#             high = mid - 1
#         else:
#             return mid
#
#     return -1
#
#
# list_1 = [12, 24, 32, 39, 45, 50, 54]
#
# result = bin_s_t(list_1, 39)
#
# print(result)


def binary_search(lst):
    n = int(input("Enter Number to search :"))

    first = 0
    last = len(lst) - 1

    while first <= last:
        mid = (first + last) // 2
        if n == lst[mid]:
            print("Number is in  ", mid + 1, " Location")
            break
        elif lst[mid] > n:
            last = mid - 1
        else:
            first = mid + 1

    if first > last:
        print(f"There is no value like {n} exist in the list")


list_1 = [12, 24, 32, 39, 45, 50, 54]

binary_search(list_1)

# Videos https://www.youtube.com/watch?v=_TVSfcPraK4
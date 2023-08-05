# def string_compression(string):
#     dict_val = {}
#
#     for i in string:
#         dict_val[i] = dict_val.get(i, 0) + 1
#
#     comp_str = ""
#
#     print(dict_val)
#
#     for k, v in dict_val.items():
#
#         if v > 1:
#             comp_str = comp_str + k + str(v)
#         else:
#             comp_str = comp_str + k
#
#     return comp_str


def string_compression(string):
    count = 1
    comp_str = ""

    for i in range(1, len(string)):

        if string[i] == string[i - 1]:
            count += 1

        else:
            comp_str = comp_str + string[i - 1]

            if count > 1:
                comp_str = comp_str + str(count)

            count = 1

    comp_str = comp_str + string[-1]

    if count > 1:
        comp_str = comp_str + str(count)

    return comp_str


string = "abbbccdeee"
print(string_compression(string))

# from typing import List
#
# class Solution:
#     def compress(self, chars: List[str]) -> int:
#
#         dict_val = {}
#         comp_str = ""
#
#         for i in chars:
#             dict_val[i] = dict_val.get(i, 0) + 1
#
#         print(dict_val)
#         for k, v in dict_val.items():
#
#             if v > 1:
#                 comp_str = comp_str + str(k) + str(v)
#             else:
#                 comp_str = comp_str + k
#
#         print(comp_str)
#         l = len(comp_str)
#
#         return l
#
# chars = ["a","a","b","b","c","c","c"]
#
# string = "abbbccdeee"
# print(Solution().compress(chars))

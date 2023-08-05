
from typing import List

from collections import Counter

""" Method 1 """
# class Solution:
#     def removeAnagrams(self, words: List[str]) -> List[str]:
#
#         res = [words[0]]
#
#         for i in range(1,len(words)):
#
#             dict_val = {}
#             dict_val1 = {}
#
#             for j in words[i]:
#                 dict_val[j] = dict_val.get(j,0) + 1
#
#             for j in words[i-1]:
#                 dict_val1[j] = dict_val1.get(j,0) + 1
#
#             # m1, m2 = Counter(words[i-1]),Counter(words[i])
#             # if m1 != m2:
#             if dict_val != dict_val1:
#
#                 res.append(words[i])
#
#         return res



# class Solution:
#     def removeAnagrams(self, words: List[str]) -> List[str]:
#
#         prev = None
#         anagram_lst = []
#
#         for i in words:
#             new_val = "".join(sorted(i))
#
#             if new_val != prev:
#
#                 anagram_lst.append(i)
#                 prev = new_val
#                 continue
#
#         return anagram_lst


print(Solution().removeAnagrams(["abba","baba","bbaa","cd","cd"]))
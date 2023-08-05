from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict_val = {}
        for word in strs:
            sortedword = "".join(sorted(word))

            if sortedword not in dict_val:

                dict_val[sortedword] = [word]

            else:

                dict_val[sortedword].append(word)

        print(dict_val)
        return list(dict_val.values())
    # print(new_dict)


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# class Solution:
#
#     def groupAnagrams(self, strs: List[str]):
#
#         res = defaultdict(list)
#
#         for s in strs:
#
#             count = [0] * 26
#
#             for c in s:
#                 count[ord(c) - ord("a")] += 1
#
#             res[tuple(count)].append(s)
#
#         return res.values()


# class Solution:
#
#     def groupAnagrams(self, strs: List[str]):
#
#         dict_val = defaultdict()
#         for word in strs:
#             sorted_word = "".join(sorted(word))
#
#             if sorted_word not in dict_val:
#                 dict_val[sorted_word] = [word]
#             else:
#                 dict_val[sorted_word].append(word)
#
#         return list(dict_val.values())

from typing import List


# Time complexity: O(N).
# Space complexity: O(1). The space complexity is O(1) because the table’s size stays constant no matter how large n is.

class Solution():
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1

            # if char not in counter:
            #     counter[char] = 1
            # else:
            #     counter[char] += 1
        # t = "nagaram"
        for char in t:
            if char not in counter:
                return False
            else:
                counter[char] -= 1

        for value in counter.values():
            if value != 0:
                return False

        return True


""" Method 2"""


class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        lst1 = [0] * 26
        lst2 = [0] * 26

        for char in s:
            lst1[ord(char) - 97] += 1

        for char in t:
            lst2[ord(char) - 97] += 1

        if lst1 == lst2:

            return True
        else:
            return False


# OR
# from collections import Counter
# class Solution:
#     def isAnagram(self,s:str,t:str)->bool:
#
#         return Counter(s)==Counter(s)

# OR

# O(nlogn)
# class Solution:
#     def isAnagram(self,s:str,t:str)->bool:
#         return  sorted(s) == sorted(t)
s = "anagram"
t = "nagaram"

print(Solution().isAnagram(s, t))

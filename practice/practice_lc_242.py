
""" Method 1"""

"""
class Solution:

    def isAnagram(self,s:str,t:str) -> bool:

        lst1 = [0] * 26
        lst2 = [0] * 26

        for char in s:
            
            lst1[ord(char) - 97] = lst1[ord(char) - 97] + 1

        for char in t:

            lst2[ord(char) - 97] = lst2[ord(char) - 97] + 1

        print(lst1)
        print(lst2)
        if lst1 == lst2:
            return True
        else:
            return False
"""


""" Method 2"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        print(len(s))
        print(len(t))
        if len(s) != len(t):
            return False

        table = {}

        for i in s:
            table[i] = table.get(i, 0) + 1

        print(table)
        for i in t:

            if i not in table:

                return False
            else:

                table[i] -= 1

        for v in table.values():

            if v != 0:
                return False

        return True


s = "anagram"
t = "nagaram"

print(Solution().isAnagram(s,t))

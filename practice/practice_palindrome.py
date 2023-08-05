
class Solution:
    def isPalindrome(self, s: str) -> bool:

        len_str = len(s)

        for i in range(0,len_str//2):

            if s[i] != s[len_str - i -1]:

                return False

        return True


""" Method """
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:

            print(s[l])
            while l < r and not s[l]:
                l += 1
            while l < r and not s[r]:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True """


string_val = "abcdeedcba"

print(Solution().isPalindrome(string_val))

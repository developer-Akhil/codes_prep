# from typing import bool

class Solution:
    def isValid(self, s: str):
        stack = []
        lookup = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for p in s:

            if p in lookup.values():

                stack.append(p)

            elif stack and stack[-1] == lookup[p]:
                stack.pop()

            else:
                return False
        return stack == []


print(Solution().isValid("()[]{}"))


# Need to look solution in "No stack O(1) space complexity O(n) time complexity solution"

class Solution(object):
    def isValid(self, s):

        stack=[]

        lookup={")":"(",
                "}":"{",
                "]":"["
                }
        for p in s:
            if p in lookup.values():
                stack.append(p)
            elif stack and stack[-1] == lookup[p]:
                stack.pop()
            else:
                return False
        return stack == []

# print(Solution().isValid("((()))("))

print(Solution().isValid("((()))"))
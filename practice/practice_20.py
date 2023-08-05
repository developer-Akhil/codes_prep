class Solution:

    def isValid(self, s: str) -> bool:

        stack = []

        lookup = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in s:

            if i in lookup.values():

                stack.append(i)
            elif stack and stack[-1] == lookup[i]:
                stack.pop()
            else:
                return False

        return stack == []


s = "(){[]{}"
# s = "()[]{}{"
print(Solution().isValid(s))

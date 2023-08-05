class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []
        for c in s:

            if stack and stack[-1][0] == c:

                stack[-1][1] += 1

            else:
                stack.append([c,1])

            if stack[-1][1] == 2:
                stack.pop()

        result=""
        for char,count in stack:

            result +=(char * count)

        return result

s = "abbaca"
# s = "azxxzy"

print(Solution().removeDuplicates(s))
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []

        for c in s:

            if stack and stack[-1][0] == c:

                stack[-1][1] += 1
            else:
                stack.append([c, 1])

            if stack[-1][1] == k:
                stack.pop()

        result = ""

        for char, count in stack:
            result += (char * count)

        return result


# s = "deeedbbcccbdaa"
# k = 2
s = "deeedbbcccbdaa"
k = 3
print(Solution().removeDuplicates(s, k))

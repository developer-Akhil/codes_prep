""" Method 1 using stack """

class Solution:

    def backspaceCompare(self, S: str, T: str) -> bool:

        stack_S = []
        stack_T = []

        for i in S:

            if i == "#" and stack_S:
                stack_S.pop()
            elif i != "#":
                stack_S.append(i)

        for i in T:

            if i == "#" and stack_T:
                stack_T.pop()
            elif i != "#":
                stack_T.append(i)

        print(stack_S)
        print(stack_T)
        if stack_S == stack_T:
            return True
        else:
            return False


""" Method 2 """

# class Solution:
#
#     def backspaceCompare(self, S: str, T: str) -> bool:
#
#         len_s = len(S) - 1
#         len_t = len(T) - 1
#
#         while (len_s >= 0) or (len_t >= 0):
#
#             if len_s = ""


# s = "ab#cj"
# t = "ad#c"

s = "y#fo##f"
t ="y#f#o##f"

print(Solution().backspaceCompare(s,t))
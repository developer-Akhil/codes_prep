# Method 1


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         print(str(x)[::-1])
#         if str(x) == str(x)[::-1]:
#             return True
#         return False


class Solution:
    def isPalindrome(self, x: int) -> bool:

        rev = 0
        y = x
        while 0 < x:
            num = x % 10

            rev = rev * 10 + num

            x = x // 10

        if y == rev:
            return True

        return False

a="akhilesh"

# print(a[::-1])
print(Solution().isPalindrome(121))

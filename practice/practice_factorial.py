class Solution:

    def getfactorial(self, n):
        if n == 0 or n == 1:

            return 1
        else:
            return n * Solution().getfactorial(n - 1)

print(Solution().getfactorial(5))


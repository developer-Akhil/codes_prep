class Solution:
    def fib(self, n: int) -> int:

        if n < 0:

            return 0

        elif n == 0:

            return 0
        elif n == 1:

            return 1
        else:

            return Solution().fib(n-1) + Solution().fib(n - 2)

print(Solution().fib(7))

class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        cur = 1
        next_val =0

        for i in range(0, n):
            next_val = prev + cur

            prev = cur
            cur = next_val

        return next_val


print(Solution().climbStairs(5))

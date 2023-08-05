class Solution:

    def trailingZeroes(self, n: int) -> int:
        count = 0
        while 0 < n:
            lead_zero = n // 5

            count += lead_zero

            n = lead_zero

        return count


print(Solution().trailingZeroes(5))

from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        num = prices[0]
        profit = 0

        for price in range(1,len(prices)):

            if num < prices[price]:
                diff = prices[price]-num
                num = min(num,prices[price])
                profit = max(profit,diff)

            else:
                num = min(num,prices[price])

        return profit


# nums = [7, 6, 4, 3, 1]
nums = [7, 1, 5, 3, 4, 6]
print(Solution().maxProfit(nums))

# Method 2
# def maxProfit(self, prices):
#
#     l, r = 0, 1
#
#     maxP = 0
#
#     while r < len(prices):
#
#         if prices[l] < prices[r]:
#
#             profit = prices[r] - prices[l]
#
#             maxP = max(maxP, profit)
#
#         else:
#             l = r
#
#         r += 1
#
#     return maxP


# class Solution:
#
#     def maxProfit(self, prices: List[int]) -> int:
#
#         num = prices[0]
#         profit = 0
#
#         for i in range(1, len(prices)):
#
#             if num < prices[i]:
#                 num = min(num, prices[i])
#                 profit = max(prices[i] - num, profit)
#             else:
#
#                 num = min(num, prices[i])
#
#         return profit

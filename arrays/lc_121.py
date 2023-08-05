from typing import List

# Note : you cannot sell a stock before you buy one

# class Solution:
#
#     def max_profit(self, prices: List[int]) -> int:
#         l, r = 0, 1                         # l=buy / r=sell
#         maxP = 0
#
#         while r < len(prices):
#             if prices[l] < prices[r]:
#                 profit = prices[r] - prices[l]          #   profit = selling price(sp) - cost price(cp)
#                 maxP = max(maxP, profit)
#
#             else:
#                 l = r
#             r += 1
#         return maxP



class Solution:

    def max_profit(self, prices: List[int]) -> int:

        l,r =0,1    #left=buy , right=sell
        max_profit =0

        while r < len(prices):
            #is it profitable transition?
            if prices[l] < prices[r]:

                profit = prices[r]-prices[l]
                max_profit = max(max_profit,profit)
            else:
                l=r
            r=r+1
        return max_profit

#

class Solution:

    def max_profit(self,prices:List[int])->int:

        max_profit = 0 # 0 / 0 /4 /4 /5 /5

        min_price = float("inf") #= 7  / 1 / 1 /1

        for price in prices:  #[7, 1, 5, 3, 6, 4]

            min_price = min(price,min_price)  #min(7,inf)=7 / min (1,7) = 1 /min(5,1) = 1 / min(3,1) = 1 / min(6,1) = 1 / min(4,1)
            profit=price-min_price            #  7 - 7 =0 / 1 - 1 = 0 / 5 - 1 = 4 / 3 - 1 =2 / 6-1 = 5 / 4-1 =3
            max_profit = max(max_profit,profit) # max(0,0) = 0 / max(0,0) = 0 / max (0,4)= 4 / max(4,2) = 4 /max(4,5)= 5 /max(5,3) =5

        return max_profit

print(Solution().max_profit([7, 1, 5, 3, 6, 4]))
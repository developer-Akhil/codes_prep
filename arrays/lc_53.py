from typing import List
# class Solution():
#
#     def max_sub_array(self,nums:List[int])->int:
#
#         current_sub = nums[0]
#         max_sub = nums[0]
#
#         for i in range(1,len(nums)):
#             current_sub=max(nums[i],nums[i]+current_sub)
#             max_sub=max(current_sub,max_sub)
#
#         return max_sub


class Solution():

    def maxSubArray(self,nums):
        # arry=[]
        maxSub = nums[0]        #5 | 5 | 9 | 9 | 15
        curSum=0                #0 | 5 | 9 | 8 | 15

        for n in nums:          #5|4|-1 | 7
            if curSum < 0:      # 5<0 | 9 < 0 | 8<0 | 15 < 0

                curSum = 0
            curSum +=n          # 0+5=5 | 5+4=9 | 9-1 =8 | 8+7=15 | 15+8 =23
            # arry.append(n)
            maxSub=max(maxSub,curSum)   #max(5,5) =5 | max(5,9)=9 | max(9,8)=9 | max(9,15)=15 | max(15,23)=23

        # print(arry)
        return maxSub



print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
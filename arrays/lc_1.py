from typing import List

# TC = O(n)
# SP = O(n)
# try for O(1)
class Solution(object):

    def twoSum(self,nums:List[int],target:int)->List[int]:

        hash_table={}

        for i in range(len(nums)):

            if nums[i] in hash_table:
                return [hash_table[nums[i]],i]
            else:
                hash_table[target-nums[i]]=i

print(Solution().twoSum([2,7,5,6,15],11))

# hash_table = {9:0,4:1}
# len(nums) = 4
# for (i=0;i++,i<=len(nums))
# (0,4) -> 0,1,2,3,4


# print(Solution().twoSum([2,7,11,15],9))
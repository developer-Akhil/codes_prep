#   https://leetcode.com/problems/climbing-stairs/
#   https://www.youtube.com/watch?v=in3Fpx8-eOY


class Solution(object):

    def climbStairs(self,n:int) -> int:
        prev = 1
        prev_to_prev=1
        curr=0

        if n <= 2:
            return n

        for i in range(1,n):
            curr=prev + prev_to_prev
            prev_to_prev=prev
            prev=curr

        return curr

print(Solution().climbStairs(5))

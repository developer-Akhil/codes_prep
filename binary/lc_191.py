class Solution():

    def hammingWeight(self,n:int)->int:


        res=0

        while n:
            res += n%2
            n=n >> 1
        return res

n = int(0b00000000000000000000000000001011)

# n = 00000000000000000000000000001011

# print(n)
print(Solution().hammingWeight(n))



class Solution(object):

    # def getSum(slef,a, b):
    #     while b:
    #         a, b = (a ^ b), (a & b) << 1
    #     return a

    def getSum(self,a:int,b:int)->int:
        while (b):
            xor = a^b
            carry = (a&b) << 1
            a,b=xor,carry
        return a

    # def getSum(self,a,b):
    #
    #     mask=0xffffffff
    #
    #     while b:
    #         sum=(a^b) & mask
    #         carry = ((a&b)<<1) & mask
    #         a=sum
    #         b=carry
    #
    #     return a


print(Solution().getSum(3,6))
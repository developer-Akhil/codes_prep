class Solution:

    def encode(self, strs):
        ans = ""

        for s in strs:
            ans += str(len(s)) + "#" + s

        return ans

    def decode(self, str):

        # 4#lint4#code4#love3#you
        res, i = [], 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1

            length = int(str[i:j])
            res.append(str[j+1:j+1+length])
            i = j+1+length
        return res
    # def decode(self, str):
    #
    #     ans = []
    #     i = 0
    #
    #     while i < len(str):
    #
    #         j = i
    #
    #         while str[j] != "$":
    #             j += 1
    #
    #         l = int(str[i:j])
    #
    #         ans.append(str[j + 1:j + 1 + l])
    #
    #         i = j + 1 + l
    #
    #     return ans


Input = ["lint", "code", "love", "you"]

print(Solution().encode(Input))

result = Solution().encode(Input)

print(Solution().decode(result))


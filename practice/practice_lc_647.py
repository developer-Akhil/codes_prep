class Solution:
    def countSubstrings(self, s: str) -> int:

        def palindromeCnt(l, r, s: str) -> int:
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            return res

        res = 0
        for i in range(len(s)):
            """ Old palindrome """
            s1 = palindromeCnt(i, i, s)
            res = res + s1

            """ Even palindrome """
            s2 = palindromeCnt(i, i + 1, s)
            res = res + s2

        return res
        # for i in range(len(s)):
        #
        #     l = r = i
        #
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         res += 1
        #         l -= 1
        #         r += 1
        #     l = i
        #     r = i + 1
        #
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         res += 1
        #         l -= 1
        #         r += 1
        #
        # return res


s = "abc"
print(Solution().countSubstrings(s))

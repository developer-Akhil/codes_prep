from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)

        dp[len(s)] = True

        for i in range(len(s)-1,-1,-1):

            for w in wordDict:

                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:

                    dp[i] = dp[i+len(w)]

                if dp[i]:
                    break

        return dp[0]

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#
#         l = len(s)
#
#         dp = [True] + [False] * l
#
#         for i in range(1, l + 1):
#
#             for j in range(0, i):
#
#                 if dp[j] and s[j:i] in wordDict:
#                     dp[i] = True
#
#         return dp[-1]


s = "leetcode"
a = ["leet", "code"]

print(Solution().wordBreak(s, a))

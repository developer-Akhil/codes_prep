from typing import List


class Solution():
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        L = len(s)
        dp = [True] + [False] * L

        for i in range(1, L + 1):               # 1,2,3,4,5,6,7,8,9

            for j in range(0,i):                  # (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8)

                if dp[j] and s[j:i] in wordDict:    # dp[7]/False and s[7:8]=e in wordDict
                    # print(s[j:i])
                    dp[i] = True                    # dp[4]=True        #dp[8]=True

        return dp[-1]


s = "leetcode"
a = ["leet","code"]

# a = ["apple", "pen"]
# s = "applepenapple"

print(Solution().wordBreak(s, a))

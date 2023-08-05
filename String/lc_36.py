class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start, end = 0, 0

        maxLen = 0

        set_num = set()

        while end < len(s):

            if s[end] not in set_num:

                set_num.add(s[end])

                maxLen = max(maxLen, len(set_num))

                end += 1
            else:

                set_num.remove(s[start])
                start += 1

        return maxLen


s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))

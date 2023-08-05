import sys


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hm = {}
        ans = 0
        l: int = 0

        for r in range(len(s)):

            hm[s[r]] = hm.get(s[r], 0) + 1

            while (r - l + 1) - max(hm.values()) > k:
                hm[s[l]] -= 1

            ans = max(ans, r - l + 1)

        return ans


s = "ABAB"
k = 2

print(Solution().characterReplacement(s, k))

# # Initialize variables
# window_start = 0
# max_length = 0
# max_count = 0
# char_count = {}
#
# # Traverse the string s
# for window_end in range(len(s)):
#     # Increment the count of the current character
#     char_count[s[window_end]] = char_count.get(s[window_end], 0) + 1
#
#     # Update the maximum count seen so far
#     max_count = max(max_count, char_count[s[window_end]])
#
#     # # Shrink the window if required
#     if window_end - window_start + 1 > max_count + k:
#         char_count[s[window_start]] -= 1
#         window_start += 1
#
#     # # Update the maximum length of the substring with repeating characters seen so far
#     max_length = max(max_length, window_end - window_start + 1)
#
# # print(char_count)
# return max_length

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start,end = 0,0
        maxlen = 0
        unqchar = set()

        while end < len(s):

            if s[end] not in unqchar:
                unqchar.add(s[end])
                end += 1

                maxlen = max(maxlen, len(unqchar))

            else:
                unqchar.remove(s[start])
                start += 1

        return maxlen


print(Solution().lengthOfLongestSubstring("abcabcbb"))

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return 0
        for i in range(len(haystack)):

            if haystack[i:i + len(needle)] == needle:
                print(i, i + len(needle))
                return i
        return -1


haystack = "hello"
needle = "ll"
print(Solution().strStr(haystack, needle))

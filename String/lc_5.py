class LongestPalendromeFinder:

    # O(n^2)
    # def longestPalindrome(self,s:str) ->str:
    #
    #     max_len=0
    #     max_word=""
    #
    #     for first in range(len(s)):
    #
    #         for second in range(first+1,len(s)+1):
    #
    #             word = s[first:second]
    #             if (word  == word[::-1]):
    #                 if max_len < len(word):
    #                     max_len=len(word)
    #                     max_word = word
    #     return  max_word

    # O(n)
    def longestPalindrome(self, s: str) -> str:

        def findLongest(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        longest = ""
        for i in range(len(s)):
            """ Old palindrome """
            s1 = findLongest(s, i, i)
            if len(s1) > len(longest): longest = s1

            """ Even palindrome """
            s2 = findLongest(s, i, i + 1)
            if len(s2) > len(longest): longest = s2

        return longest


print(LongestPalendromeFinder().longestPalindrome("abacabc"))

# print(LongestPalendromeFinder().longestPalindrome("abbacakbc"))
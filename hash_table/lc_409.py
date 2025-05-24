class Solution:
    def longestPalindrome(self, s: str) -> int:

        # initialize hashmap and fill in count for each letter in s
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1

        # initialize output and flag
        longest = 0
        hasOdd = False

        for value in counts.values():
            if value % 2 == 0:
                longest += value
            else:
                longest += (value - 1)
                hasOdd = True

        # if odd letter available, add 1 to length
        if hasOdd:
            longest += 1

        # return length of longest palindrome
        return longest

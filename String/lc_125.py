# Time: O(n)O(n)
# Space: O(1)O(1)

class Solution():

    def isPalindrome(self,s:str)->bool:

        l,r =0,len(s)-1

        while l<r:
            while l<r and not self.alpahNum(s[l]):
                l +=1

            while l<r and not self.alpahNum(s[r]):
                r -=1

            if s[l].lower() != s[r].lower():
                return False

            l,r=l+1,r-1

        return True

    def alpahNum(self,c):
        return (ord('A') <= ord(c) <= ord('Z')
                or ord('0') <= ord(c) <= ord('9')
                or ord('a') <= ord(c) <= ord('z'))


s = "A man, a plan, a canal: Panama"

print(Solution().isPalindrome(s))


'''
Generate all rotations of a given string
Difficulty Level : Easy
Last Updated : 02 Nov, 2021
Given a string S. The task is to print all the possible rotated strings of the given string.

Examples:

Input : S = "geeks"
Output : geeks
         eeksg
         eksge
         ksgee
         sgeek

Input : S = "abc"
Output : abc
         bca
         cab
'''

#O(n^2)
def printRotatedString(string):

    n=len(string)

    temp=string+string   # abcabc

    for i in range(n):          # 0,1,2

        for j in range(n):      # 0,1,2 | 0

            print( temp[i+j],end="")   # a,b,c  | b,c,a | c,a,b
        print()

if __name__ == "__main__":
    string = "abc"
    printRotatedString(string)
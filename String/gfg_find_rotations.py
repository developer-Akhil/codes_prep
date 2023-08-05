'''
Minimum rotations required to get the same string
Difficulty Level : Medium
Last Updated : 28 Dec, 2021
Given a string, we need to find the minimum number of rotations required to get the same string.
Examples:


Input : s = "geeks"
Output : 5

Input : s = "aaaa"
Output : 1
'''

def findRotations(string):

    tmp = string + string

    n = len(string)

    for i in range (1,n+1):

        #substring from i index of original string size
        substring = tmp[i:i+n]

        # if substring matches with original string then we will come out of the loop

        if substring == string:
            return i

    return n

string="abc"
print(findRotations(string))
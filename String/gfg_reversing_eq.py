'''
Reversing an Equation
Difficulty Level : Basic
Last Updated : 04 Jan, 2021
Given a mathematical equation using numbers/variables and +, -, *, /. Print the equation in reverse.

Examples:

Input : 20 - 3 + 5 * 2
Output : 2 * 5 + 3 - 20

Input : 25 + 3 - 2 * 11
Output : 11 * 2 - 3 + 25

Input : a + b * c - d / e
Output : e / d - c * b + a
'''


def reverseEquation(s):
    # Reverse String
    result = ""
    for i in range(len(s)):

        # A space marks the end of the word
        if (s[i] == '+' or s[i] == '-' or s[i] == '/' or s[i] == '*'):

            # insert the word at the beginning
            # of the result String
            result = s[i] + result

        # insert the symbol
        else:
            # insert the word at the beginning
            result = s[i] + result
    return result


if __name__ == '__main__':
    # Driver Code
    s = "a+b*c-d/e"
    print(reverseEquation(s))

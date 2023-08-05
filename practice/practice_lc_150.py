from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for i in tokens:

            if i == "+":
                stack.append(stack.pop() + stack.pop())

            elif i == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b - a))
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))

            else:
                stack.append(int(i))

        return stack[-1]


tokens = ["4", "13", "5", "/", "+"]
print(Solution().evalRPN(tokens))

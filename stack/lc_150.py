from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for op in tokens:

            if op == "+":
                stack.append(stack.pop() + stack.pop())

            elif op == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)

            elif op == "*":

                stack.append(stack.pop() * stack.pop())

            elif op == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))

            else:

                stack.append(int(op))

        return stack[0]


# print(Solution().evalRPN(["2", "1", "+", "3", "*"]))

print(Solution().evalRPN(["4", "13", "5", "/", "+"]))

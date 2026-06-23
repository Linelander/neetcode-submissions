from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        print(7/-3)
        print(7//-3)
        
        
        stack = []
        for t in tokens:
            if t == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(t))
        return stack[0]

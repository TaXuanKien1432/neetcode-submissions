class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for string in tokens:
            if string == "+":
                stack.append(stack.pop() + stack.pop())
            elif string == "*":
                stack.append(stack.pop() * stack.pop())
            elif string == "-":
                second, first = stack.pop(), stack.pop()
                stack.append(first - second)
            elif string == "/":
                second, first = stack.pop(), stack.pop()
                stack.append(int(first / second))
            else:
                stack.append(int(string))
        
        return stack[0]
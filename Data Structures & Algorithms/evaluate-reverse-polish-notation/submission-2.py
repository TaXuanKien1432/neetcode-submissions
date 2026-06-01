class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        
        for string in tokens:
            if string not in operators:
                stack.append(string)
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                if string == "+":
                    result = first + second
                elif string == "-":
                    result = first - second
                elif string == "*":
                    result = first * second
                elif string == "/":
                    result = int(first / second)
                stack.append(result)
        
        return int(stack[-1])
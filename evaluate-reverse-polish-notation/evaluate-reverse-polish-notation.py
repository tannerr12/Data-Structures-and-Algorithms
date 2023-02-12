class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        
        for char in tokens:
            
            if char.lstrip("-").isdigit():
                
                stack.append(char)
                
            else:
                right = int(stack.pop())
                left = int(stack.pop())
                if char == "*":
                    stack.append(left * right)
                elif char == "/":
                    stack.append(left / right)
                elif char == "+":
                    stack.append(left + right)
                elif char == "-":
                    stack.append(left - right)
        
        
        return int(stack[0])
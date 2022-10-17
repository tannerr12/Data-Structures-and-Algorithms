class Solution:
    def isValid(self, s: str) -> bool:
       
        stack = []
            
        for char in s:
            if char == "{" or char == "[" or char == "(":
                stack.append(char)
            elif char == "}":
                if len(stack) == 0 or stack[len(stack) -1] != "{":
                    return False
                else:
                    stack.pop()
            elif char == "]":
                if len(stack) == 0 or stack[len(stack) -1] != "[":
                    return False
                else:
                    stack.pop()
            elif char == ")":
                if len(stack) == 0 or stack[len(stack) -1] != "(":
                    return False
                else:
                    stack.pop()
        return False if stack else True
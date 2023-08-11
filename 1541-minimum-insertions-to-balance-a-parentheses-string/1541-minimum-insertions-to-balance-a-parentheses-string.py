class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        res = 0
        for i in range(len(s)):
            
            if s[i] == '(':
                if stack and stack[-1] == 1:
                    res +=1
                    stack.pop()
                stack.append(0)
            else:
                if not stack:
                    stack.append(0)
                    res += 1
                val = stack.pop()
                if val == 0:
                    stack.append(1)
        
        
        #print(res)
        #print(stack)
        
        while stack:
            val = stack.pop()
            res += 2 - val
        
        
        return res
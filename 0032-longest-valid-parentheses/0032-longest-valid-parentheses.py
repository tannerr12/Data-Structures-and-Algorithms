class Solution:
    def longestValidParentheses(self, s: str) -> int:

     
        
        close = 0
        op = 0
        
        res = 0
        
        for i in range(len(s)):
            
            if s[i] == '(':
                op+=1
                    
            else:
                if close + 1 > op:
                    op = 0
                    close = 0
                else:
                    close +=1
        
            if op == close:
                res = max(res, op + close)
        
        
        close = 0
        op = 0
        for i in range(len(s) -1,-1,-1):
            
            if s[i] == ')':
                op+=1
                    
            else:
                if close + 1 > op:
                    op = 0
                    close = 0
                else:
                    close +=1
        
            if op == close:
                res = max(res, op + close)
        return res
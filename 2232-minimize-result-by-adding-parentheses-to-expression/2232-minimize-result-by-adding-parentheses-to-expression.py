class Solution:
    def minimizeResult(self, expression: str) -> str:
        
        pos = 0
        for i, char in enumerate(expression):
            if char == '+':
                pos = i
        
        res = [float('inf'),'']
        def dfs(i,j):
            nonlocal res
            nonlocal pos
            if i >= pos or j <= pos+1:
                return 
            
            if i == 0 and j == len(expression):
                val = '(' + expression + ')'
            elif j == len(expression):
                 val = expression[:i] + '*(' + expression[i:j] + ')' + expression[j:]
            elif i == 0:
                 val = expression[:i] + '(' + expression[i:j] + ')*' + expression[j:]
            else:
                val = expression[:i] + '*(' + expression[i:j] + ')*' + expression[j:]

            calc = eval(val)
            if calc < res[0]:
                res = [calc, val.replace('*', '')]
            
            #shift '(' ->
            
            dfs(i+1,j)
            
            #shift ')' <-
            dfs(i,j-1)
        
        dfs(0,len(expression))
        
        return res[1]
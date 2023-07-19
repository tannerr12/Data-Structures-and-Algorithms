class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        @cache
        def dfs(exp,syb):
            
            stack = []
            res = True
            if syb == '|':
                res = False
            for i in range(len(exp)):
                
                if exp[i]== '(':
                    stack.append(i)
                if exp[i] == ')':
                    pos = stack.pop()
                    if len(stack) == 0:
                        symbol = exp[pos-1]
                        if syb == '&':
                            res = res and dfs(exp[pos+1:i],symbol)
                        elif syb == '|':
                            res = res or dfs(exp[pos+1:i],symbol)
                        else:
                            res = res and not(dfs(exp[pos+1:i],symbol))
                
                if len(stack) == 0 and exp[i] == 'f':
                    if syb == '&':
                        res = res and False
                    elif syb == '|':
                        res = res or False
                    else:
                        res = res and (not False)
                elif len(stack) == 0 and exp[i] == 't':
                    if syb == '&':
                        res = res and True
                    elif syb == '|':
                        res = res or True
                    else:
                        res = res and (not True)
                        
            
            return res
        
        return dfs(expression, '&')
                
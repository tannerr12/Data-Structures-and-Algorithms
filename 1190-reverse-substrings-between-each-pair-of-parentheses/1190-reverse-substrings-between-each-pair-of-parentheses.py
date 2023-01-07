class Solution:
    def reverseParentheses(self, s: str) -> str:
        @cache
        def dfs(i):
            if i >= len(s):
                return ''
            
            bracket = 1
            res =''
            while bracket:
                if i >= len(s):
                    break
                if s[i] == '(':
                    val, j = dfs(i+1)
                    res += val
                    i = j
                elif s[i] == ')':
                    break
                
                else:
                    res += s[i]
                
                
                i+=1
            
            return res[::-1],i
        
        return dfs(0)[0][::-1]
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        @cache
        def dfs(i, count, last2, last1):
            
            if i >= len(num) and count >= 3:
                return True
            elif i >= len(num):
                return False
            
            res = False
            
            if num[i] == '0':
                val = 0
                if val == last2 + last1 or last2 == float('inf') or last1 == float('inf'):
                    res = res or dfs(i+1, count + 1, last1, val)
            else:
                for j in range(i, len(num)):

                    val = int(num[i:j+1])

                    if val == last2 + last1 or last2 == float('inf') or last1 == float('inf'):
                        res = res or dfs(j+1, count + 1, last1, val)

                
            return res    
        
        
        return dfs(0,0,float('inf'),float('inf'))
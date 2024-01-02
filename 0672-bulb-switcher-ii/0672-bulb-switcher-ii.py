class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        n = min(n,3)
        if presses == 0:
            return 1
        if n == 1:
            return 2
        if n == 2 and presses == 1:
            return 3
        
        s = set()
        
        
        #1
        @cache
        def dfs(p,a,o,e,k):
            
            if p == presses:
                s.add((a,o,e,k))
                return 
            
            dfs(p+1, (a+1) % 2,o,e,k)
            dfs(p+1, a,(o+1) % 2,e,k)
            dfs(p+1,a,o,(e+1) % 2,k)
            dfs(p+1,a,o,e,(k+1) % 2)
            
        
        dfs(0,0,0,0,0)
        if n == 2:
            return min(4, len(s))
        elif n == 1:
            return min(2, len(s))
        return len(s)
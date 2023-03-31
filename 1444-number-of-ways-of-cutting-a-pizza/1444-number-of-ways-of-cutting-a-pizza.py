class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        n,m = len(pizza), len(pizza[0])
        MOD = (10 **9 + 7)
        @cache
        def countAppleByRow(x,y):
            if y == m:
                return 0
            p = 0
            if pizza[x][y] == 'A':
                p = 1
            return countAppleByRow(x,y+1) + p
        @cache
        def countApple(x,y):
            if x == n:
                return 0
            return countAppleByRow(x,y) + countApple(x+1, y)
        
        #check all splits than check each grid for an apple left and right
        
        def containsApple(ax,ay,bx,by):
            return countApple(ax,ay) - countApple(bx + 1, ay) - countApple(ax,by+1) + countApple(bx+1,by+ 1) > 0
        
        @cache
        def dfs(x,y,k):
            nonlocal n
            nonlocal m
            
            if k == 0:
                if containsApple(x,y, n-1,m-1):
                    return 1
                return 0
            
            res = 0 
            
            for i in range(x,n-1):
                if containsApple(x,y,i,m-1) and containsApple(i+1, y,n-1, m-1):
                    res += dfs(i+1,y,k-1)
                    res %= MOD
            
            for i in range(y, m-1):
                if containsApple(x, y,n-1, i) and containsApple(x,i+1, n-1, m-1):
                    res += dfs(x, i+1, k-1)
                    res %= MOD
            """
            av = set()
            ah = set()
            for a in range(i, n):
                for b in range(j, m):
                    if pizza[a][b] == 'A':
                        if b not in av:
                            #split vertical
                            res += dfs(i, b + 1,cuts + 1)
                            av.add(b)
                        if a not in ah:
                            #split horizontal
                            res += dfs(a+1, j, cuts + 1)
                            ah.add(a)
            """
            return res % MOD
        
        
        return dfs(0,0,k-1) % MOD
                        
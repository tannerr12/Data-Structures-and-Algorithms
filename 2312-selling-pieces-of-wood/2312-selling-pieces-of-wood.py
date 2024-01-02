class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        total = m * n
        mp = defaultdict(int)
        
        for x,y,p in prices:
            mp[(x,y)] = p
        
        @lru_cache(maxsize = 100000)
        def dfs(h, w):
            
            res = mp[(h,w)]
            
            #all possible cuts
            for i in range(1, h //2 + 1):
                left = dfs(i, w)
                right = dfs(h-i, w)
                res = max(res, left + right)
            for i in range(1, w // 2 + 1):
                left = dfs(h,i)
                right = dfs(h,w-i)
                res = max(res, left + right)
                
            return res
            
        
        return dfs(m,n)
            
            
            
            
        '''   
        while best:
            b = best.pop()
            blocks = 0
            blocks += m // b[1]
            blocks *= n // b[2]

            score += blocks * b[3]
            
            remh = m % b[1]
            remw = n % b[2]
            
            #print(score)

        #def dfs()
        return score
        '''
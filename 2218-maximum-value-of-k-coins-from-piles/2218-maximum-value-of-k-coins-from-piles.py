class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        
        #pmap = defaultdict(list)
        
        #for i in range(len(piles)):
        #    pmap[i].append(0)
        #    for j in range(len(piles[i])):
        #        pmap[i].append(pmap[i][-1] + piles[i][j])
        
        #print(pmap)
        
        @cache
        def dfs(i,rem):
            
            
            if rem == 0:
                return 0
            
            if i >= len(piles):
                return float('-inf')
            
            res = 0
            
            #skip number
            res = max(res,dfs(i+1, rem))
            run = 0
            for j in range(min(len(piles[i]), rem)):
                run += piles[i][j]
                res = max(res, dfs(i+1,rem-j-1) + run)
                
                
            return res
        
        return dfs(0,k)
        
        '''
        def dfs(rem):
            
            if rem == 0:
                return 0
            
            res = 0
            for i in range(len(piles)):
                
                if pmap[i] == len(piles[i]):
                    continue
                
                pmap[i] += 1
                res = max(res, dfs(rem -1) + piles[i][pmap[i] -1])
                pmap[i] -= 1
                
            
            return res
        
        return dfs(k)
        
        '''
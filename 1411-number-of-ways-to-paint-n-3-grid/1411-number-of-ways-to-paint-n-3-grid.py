class Solution:
    def numOfWays(self, n: int) -> int:
        #print(len(list(itertools.permutations(['r','r','r', 'y','y','y','g','g','g'], 3))))
        MOD = 10 ** 9 + 7
        colors = []
        
        def buildColors(curr):
            
            if len(curr) == 3:
                colors.append(curr)
                return
            for val in 'rgy':
                if len(curr) == 0 or curr[-1] != val:
                    buildColors(curr + val)
            
        
        @cache
        def dfs(i,prev):
            
            if i > n:
                return 1
            
            res = 0
            #add layer
            #create map of colors
            for val in colors:
                if prev[0] != val[0] and prev[1] != val[1] and prev[2] != val[2]:    
                    res += dfs(i+1,val)
            res %= MOD
            return res
        
        
        buildColors('')
        return dfs(1,'000')
            
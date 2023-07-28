class Solution:
    def numOfWays(self, n: int) -> int:
        #print(len(list(itertools.permutations(['r','r','r', 'y','y','y','g','g','g'], 3))))
        MOD = 10 ** 9 + 7
        
        @cache
        def dfs(i,prev,last):
            
            if i > n:
                return 1
            
            res = 0
            #add layer
            if len(last) == 3:
                res += dfs(i+1,last,'')
            else:
                for val in 'rgy':
                    if last and val == last[-1]:
                        continue
                    if val == prev[len(last)]:
                        continue
                    res += dfs(i,prev,last + val)
                    
            res %= MOD
            return res
        
        return dfs(1,'000','')
            
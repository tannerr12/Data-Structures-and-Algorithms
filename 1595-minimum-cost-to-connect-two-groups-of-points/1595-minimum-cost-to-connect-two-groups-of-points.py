class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
            
            

            m = 2 ** len(cost[0]) -1
            m2 = 2 ** len(cost) -1
            
            mp = defaultdict(lambda:float('inf'))
            for i in range(len(cost)):
                for j in range(len(cost[0])):
                    mp[j] = min(mp[j], cost[i][j])
            print(mp)
            
            @cache
            def dfs(i,maskA):
                
                if i >= len(cost):
                    t = 0
                    for j in range(len(cost[0])):
                        if maskA & (1 << j) == 0:
                            t += mp[j]
                    return t

                res = float('inf')
                
                for j in range(len(cost[i])):
                    #take 
                    res = min(res, dfs(i+1, maskA | (1 << j)) + cost[i][j])
                    
                return res
            
            
            return dfs(0,0)
            
                
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:

        #dp = [[0 for j in range(len(special) +1)] for i in range(len(needs) +1)]

        
        memo = {}
        def dfs(i,tneeds,bitmask,mult):
            
            
            if i >= len(special):
                cost = 0
                for n in range(len(tneeds)):
                    cost += tneeds[n] * price[n]
                return cost
            
            
            if (i,bitmask,mult) in memo:
                return memo[(i,bitmask,mult)]
            
            t = tneeds.copy()
            #take special
            dont = False
            res = float('inf')
            for j in range(50):
                for v in range(len(tneeds)):
                    if t[v] >= special[i][v]:
                        t[v] -= special[i][v]
                    else:
                        dont = True
                        break
                if not dont:
                    res = min(res,dfs(i+1,t,bitmask | (1 << i),j) + special[i][-1] * (j + 1))
                else:
                    break
                #for v in range(range(tneeds[0])):
                #    tneeds[v] += special[i][v]
            
            
            #leave special
            res = min(res, dfs(i+1,tneeds,bitmask,mult))
            
            memo[(i,bitmask,mult)] = res
            return res
        
        
        return dfs(0,needs,0,0)
        
        
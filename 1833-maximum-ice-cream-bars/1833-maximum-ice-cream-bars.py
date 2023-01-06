class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """ 
        costs.sort()
        res = 0
        for i in range(len(costs)):
            
            if costs[i] > coins:
                return res
            
            coins -= costs[i]
            res +=1
        
        return res
        """
        
        def Solution2(coins):
            
            h = Counter(costs)
            
            res = 0
            for i in range(1,10**5 +1):
                if i > coins:
                    break
                if i in h:
                    
                    v = min(coins // i, h[i])
                    res += v
                    coins -= v * i
            
            
            return res
        
        return Solution2(coins)
            
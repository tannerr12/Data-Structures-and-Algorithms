class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        res = 0
        for i in range(len(costs)):
            
            if costs[i] > coins:
                return res
            
            coins -= costs[i]
            res +=1
        
        return res
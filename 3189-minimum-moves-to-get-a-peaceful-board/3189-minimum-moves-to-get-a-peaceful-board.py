class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        
        
        rooks.sort()
        
        cost = 0
        
        for i in range(len(rooks)):
            x,y = rooks[i]
            cost += abs(x - i)
            rooks[i] = [i, y]
            
        
        
        rooks.sort(key=lambda x: x[1])
        
        for i in range(len(rooks)):
            x,y = rooks[i]
            cost += abs(y - i)
            rooks[i] = [x, i]
            
        
        
        return cost
            
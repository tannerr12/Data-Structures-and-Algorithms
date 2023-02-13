class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        target = high - low
        
        if low % 2 or high % 2:
            res = target //2 + 1 
        else:
            res = target //2
            
        return res
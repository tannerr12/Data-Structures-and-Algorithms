class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        
        x = 1
        for i,c in enumerate(coins):
            
            if c <= x:
                x+=c
            
        return x
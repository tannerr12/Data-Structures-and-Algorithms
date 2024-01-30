class Solution:
    def maxScore(self, prices: List[int]) -> int:
        
        start = defaultdict(int)
        
        
        for i in range(len(prices)):
            
            pos = prices[i] - i
            start[pos] += prices[i]
        
        return max(start.values())
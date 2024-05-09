class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        hap = []
        for val in happiness:
            hap.append(-val)
        
        heapify(hap)
        
        rounds = 0
        res = 0
        for i in range(k):
            
            val = heappop(hap)
            val = -val
            res += max(0, val - rounds)
            
            rounds += 1
        
        return res
            
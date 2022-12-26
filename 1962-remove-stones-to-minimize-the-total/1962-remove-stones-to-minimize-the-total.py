class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        
        for p in piles:
            heappush(heap, -p)
        
        for i in range(k):
            if not heap:
                return 0
            
            val = heappop(heap)
            val = -val
            v = val - (val //2)
            heappush(heap,-v)
            
        
        
        res = 0
        while heap:
            res -= heappop(heap)
        
        
        return res
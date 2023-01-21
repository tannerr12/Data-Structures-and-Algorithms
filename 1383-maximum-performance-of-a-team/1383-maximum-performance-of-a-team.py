class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        
        arr = []
        
        for x,y in zip(speed,efficiency):
            
            arr.append((y,x))
            
        
        
        arr.sort(reverse=True)
        MOD = (10**9)+7
        heap = []
        total = 0
        res = 0 
        
        for i in range(len(arr)):
            total += arr[i][1]
            heappush(heap, arr[i][1])
            
            if len(heap) > k:
                
                total -= heappop(heap)
            
            
            res = max(res, total * arr[i][0])
            
        
        
        return res % MOD
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        
        minHeap = []
        maxHeap = 0
        
        for num in nums:
            tmp = num
            
            while num % 2 == 0:
                num //= 2
            
            heappush(minHeap, (num, max(tmp,num * 2)))
            maxHeap = max(maxHeap, num)
            
        
        res = float('inf')
        
        while len(minHeap) == len(nums):
            
            val,mx = heappop(minHeap)
            
            res = min(res, maxHeap - val)
            
            if mx > val:
                
                heappush(minHeap, (val * 2, mx))
                maxHeap = max(maxHeap, val*2)
        return res
        
            

            
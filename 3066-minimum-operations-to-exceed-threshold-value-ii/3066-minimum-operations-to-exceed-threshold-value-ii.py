class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        
        #400k * log 
        
        heapify(nums)
        
        count = 0
        
        
        while nums and nums[0] < k:
            
            x = heappop(nums)
            y = heappop(nums)
            
            new = x * 2 + y
            
            heappush(nums, new)
            
            count += 1
        
        
        return count
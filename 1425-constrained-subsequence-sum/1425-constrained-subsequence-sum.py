class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        #at any point there will be a best value and if that value is > 0 we should use it since the cost is free
        #we may have a current sum and a best sum
        
        #cur could be 10 + -2 = 8 
        
        #we need to be careful about going over the distance limit
        
        heap = [[0,0]]
        res = float('-inf')
        for i in range(len(nums)):
            
            while heap[0][1] < i - k:
                heappop(heap)
                
            val, idx = heap[0]
            val = -val
            
            if val >= 0:
                res = max(res, val + nums[i])
                heappush(heap, [-(val + nums[i]), i])
            else:
                res = max(res, nums[i])
                heappush(heap, [-nums[i], i])
        
        return res
            
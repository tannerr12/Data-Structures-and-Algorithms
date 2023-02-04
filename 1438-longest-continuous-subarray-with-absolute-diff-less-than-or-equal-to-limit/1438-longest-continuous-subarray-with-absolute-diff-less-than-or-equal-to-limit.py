class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        
        l = 0
        
        res = 0
        heapmin = []
        heapmax = []
        for i in range(len(nums)):
            
            
            heappush(heapmin,(nums[i],i))
            heappush(heapmax,(-nums[i],i))
            while heapmin and heapmax and abs(heapmin[0][0] + heapmax[0][0]) > limit:
                l+=1
                while heapmax and heapmax[0][1] < l:
                    heappop(heapmax)
                while heapmin and heapmin[0][1] < l:
                    heappop(heapmin)
                
                
            
            res = max(res, i-l+1)
            
        
        
        return res
            
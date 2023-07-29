class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        calcMax = nums[-1] - nums[0] - len(nums) + 1
        if k > calcMax:
            k-= calcMax
            return nums[-1] + k
        
        start = nums[0]
        
        def binary(l,r):
            
            
            while l < r:
                
                mid = (l+r) // 2
                
                calc = nums[mid] - start - (mid)

                if calc >= k:
                    r = mid -1
                else:
                    l = mid +1
                
            
            return l
        
        idx = binary(0,len(nums))
        if idx > 0:
            if nums[idx] - nums[0] - (idx) >= k:
                idx -=1
        calc = nums[idx] - nums[0] - (idx) 
        k-= calc
        return nums[idx] + k
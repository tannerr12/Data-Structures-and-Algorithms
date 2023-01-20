class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        
        l = 0
        
        res= 0
        total = 1
        size = 0
        s = 0
        mx = (len(nums) * (len(nums) +1)) //2
        for i in range(len(nums)):
            
            
            s += nums[i]
            size +=1
            

            while s*size >= k:
                res += 1+ ((len(nums)-1) - i)
                s -= nums[l]
                l+=1
                size -=1
            
            
            
        
        
        return mx - res
            
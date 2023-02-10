class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        
        l,r = 0, len(nums)-1
        res = 0
        
        while l < r:
            
            if nums[l] == nums[r]:
                l+=1
                r -=1
                continue
            
            
            if r - l > 1 and nums[l] + nums[l+1] == nums[r] + nums[r-1]:
                l+=2
                r-=2
                res +=2
            
            elif nums[l] + nums[l+1] == nums[r]:
                l+=2
                r-=1
                res +=1
            
            elif nums[r] + nums[r-1] == nums[l]:
                r-=2
                l+=1
                res +=1
            
            else:
                if nums[r] > nums[l]:
                    l+=1
                    nums[l] += nums[l-1]
                    res +=1
                else:
                    r -=1
                    nums[r] += nums[r+1]
                    res +=1
            
        
        return res 
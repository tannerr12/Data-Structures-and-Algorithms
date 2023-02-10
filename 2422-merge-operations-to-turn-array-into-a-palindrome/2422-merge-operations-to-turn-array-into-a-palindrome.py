class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        
        l,r = 0, len(nums)-1
        res = 0
        
        while l < r:
            
            if nums[l] == nums[r]:
                l+=1
                r -=1
                continue

            if nums[r] > nums[l]:
                l+=1
                nums[l] += nums[l-1]
                res +=1
            else:
                r -=1
                nums[r] += nums[r+1]
                res +=1


        return res 
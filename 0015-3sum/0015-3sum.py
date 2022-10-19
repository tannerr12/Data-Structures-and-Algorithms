class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        
        l,r = 0,0
        res = []
        i= 0
        while i < len(nums):
            while i > 0 and i < len(nums) and nums[i-1] == nums[i]:
                i+=1
            
            l = i +1
            r = len(nums) -1

            
            while l < r:
                sumr = nums[i] + nums[l] + nums[r]
                if (sumr == 0):
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l-1] == nums[l]:
                         l+=1
                elif sumr > 0:
                    r-=1
                    while l < r and nums[r+1] == nums[r]:
                         r-=1
                
                elif sumr < 0:
                    l+=1
                    while l < r and nums[l-1] == nums[l]:
                         l+=1
                    
            i+=1
        return res
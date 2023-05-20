class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        
        #start = -((10 ** 5) + 1)
        last = float('-inf')
        used = False
        nums = [last] + nums
        #print(nums)
        for i in range(2, len(nums)):
            
            if nums[i] < nums[i-1] and not used:
                if nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i-2]
                else:
                    nums[i] = nums[i-1]
                
                used = True
            elif nums[i] < nums[i-1] and used:
                return False
        
        return True
                
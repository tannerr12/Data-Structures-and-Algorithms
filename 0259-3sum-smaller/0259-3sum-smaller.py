class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        nums.sort()
  
        res = 0
        r = len(nums) -1
        for i in range(len(nums)):
            r = len(nums) -1
            for j in range(i+1,len(nums)):
                tar = target - nums[i] - nums[j]
                
                while r > j and nums[r] >= tar:
                    r -=1
                if r > j:
                    res += r - j
                
        return res
                
                
                
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        print(nums)
        res = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                tar = target - nums[i] - nums[j]
                idx = bisect_left(nums, tar)
                idx -=1
                if idx > j:
                    res += idx - j
              #  print(tar)
              #  print(idx)
                
        return res
                
                
                
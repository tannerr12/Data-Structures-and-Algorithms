class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        def check(k):
            extra = 0
            for i in range(len(nums) -1,-1,-1):
                if nums[i] + extra > k:
                    extra += nums[i] - k
                else:
                    extra =0
            return extra == 0
        
        
        
        left,right = 0, max(nums)
        
        while left < right:
            m = (left + right) // 2
            
            if check(m):
                right = m
            else:
                left = m + 1
        return left
        
              



        
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        
        h = collections.defaultdict(int)
        offset = 0
        for i in range(len(nums)):
            
            
            h[nums[i]]+= 1
            
            if h[nums[i]] > 2:
                nums[i] = None
                offset +=1
            
            else:
                nums[i - offset] = nums[i]
                
        
        
        print(nums)
        return len(nums) - offset
class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        
        #&ing only makes things smaller
        
        target = nums[0]
        
        for i in range(len(nums)):
            target &= nums[i]
        
        if target > 0:
            return 1
        print(target)

        splits = []
        val = nums[0]
        for i in range(1,len(nums)):
            
            if val == target:
                splits.append(i)
                val = nums[i]
                
            val &= nums[i]
            
        
        #print(splits)
        
        if val == target:
            return len(splits) + 1
        else:
            idx = splits[-1] - 1
            
            while idx >= 0 and val != target:
                if splits and idx == splits[-1] -1:
                    splits.pop()
                
                val &= nums[idx]
                idx -=1
                
            
        
            return len(splits) + 1
            
            
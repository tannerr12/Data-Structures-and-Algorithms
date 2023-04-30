class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        '''
        res = 0
        for i in range(len(nums) -2,-1,-1):
            if i % 2 == 0 and nums[i] == nums[i+1]:
                res +=1
        
        
        if (len(nums) - res) % 2:
            res +=1
        
        '''
        r2 = 0
        
        i = 0
        shift = 0
        while i < len(nums) -1:
            if (i - shift) % 2 == 0 and nums[i] == nums[i+1]:
                shift +=1
                r2 +=1
            
            i+=1
            
        if (len(nums) - r2) % 2:
            r2 +=1
        #print(r2)
        return r2
                
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        @cache
        def pd(x):
            best = -1
            for i in range(x//2,1,-1):
                if (x / i) % 1 == 0:
                    return i
            
            
            return best
        
        
        count = 0
        for i in range(len(nums)-2,-1,-1):
            
            nxt = nums[i+1]
            
            while nums[i] > nxt:
                
                find = pd(nums[i])
                
                if find == -1:
                    return -1
                
                nums[i] = nums[i] // find
                count += 1
        
        return count
            
            
                
            
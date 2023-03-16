class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        #0s dont matter
        
        
        
        p = 0
        
        for i in range(1,len(nums)):
        
                p = (nums[i] * i) + p
                
        
        #print(p)
        
        
        total = sum(nums)
        """
        #brute force how can we compress this into linear
        res = 0
        for i in range(len(nums)):
            j = i + 1
            j %= len(nums)
            count = 1
            val = 0
            while j != i:
                
                val += nums[j] * count
                count +=1
                j+=1
                j %= len(nums) 
            
            res = max(res,val)
        
        return res
        """
        
        #problem is number * distance from position
        # y + z = a /2 /1
        # 
        
        # left pointer
        r = len(nums) -1
        res = float('-inf')
        for l in range(len(nums)):
            res = max(res, p)
            
            r +=1
            r %= len(nums)
            
            calc = (p - total) + nums[r] * len(nums)
            p = calc
        
        return res
            
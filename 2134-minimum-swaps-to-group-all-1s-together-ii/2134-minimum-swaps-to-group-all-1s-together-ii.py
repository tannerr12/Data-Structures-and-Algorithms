class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        if 1 not in count or 0 not in count:
            return 0
        
        cright = Counter(nums[-count[1]+1:])
        
        one = 0
        
        if 1 in cright:
            one = cright[1]
        l = len(nums) - count[1] +1  
        res = count[1]
        for i in range(len(nums)):
            
            if nums[i] == 1:
                one+=1
                
            
            gap = 0
            
            if l >= i:
                
                gap = len(nums) - l + i +1
            else:
                gap = i - l + 1
            
            
            while gap > count[1]:

                if nums[l] == 1:
                    one -=1
                
                l +=1
                l %= len(nums)
                
                if l >= i:
                    gap = len(nums) - l + i +1
                else:
                    gap = i - l + 1
            
            
            res = min(res, count[1] - one)
        
        
        return res
            
        
        
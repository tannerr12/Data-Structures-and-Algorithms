class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        
        xor = [0] * 32
        l = len(nums) -1
        res = [0] * len(nums)
        last = len(nums) -1
        cur = 0
        roll = 0
    
        for i in range(len(nums)-1,-1,-1):
 
            for j in range(32):
                if nums[i] & (1 << j) > 0:
                    xor[j] += 1
                    cur |= (1 << j)
            roll |= nums[i]
            
            while cur == roll and i <= l:
                for j in range(32):
                    if nums[l] & (1 << j) > 0:
                        xor[j] -= 1
                        if xor[j] == 0:
                            cur = cur ^ (1<<j)
                
                l-=1
                
            
            
            res[i] = l - i + 2
        
        
        return res
        
                
            
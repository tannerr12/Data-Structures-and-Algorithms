class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        h = {0:0}
        
        s = 0
        res =0
        for i in range(len(nums)):
            num = nums[i]
            s += num
            
            
            if s % k in h:
                
                h[s%k] +=1
                res += h[s%k]
                
            else:
                h[s%k] = 0
            
        
        return res
            
            
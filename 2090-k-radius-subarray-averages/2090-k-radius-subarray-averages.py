class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        prefix = []
        prefix.append(0)
        for i in range(len(nums)):
            if i ==0 :
                prefix.append(nums[i])
            else:
                prefix.append(nums[i] + prefix[-1])
        
        res = [-1] * len(nums)
        
        
        for i in range(k,len(nums) - k):
            
            calc = (prefix[(i+1) + k] - prefix[(i+1) - (k+1)]) // ((k*2)+1)
            
            res[i] = calc
        
        return res
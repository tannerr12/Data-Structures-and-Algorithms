class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        h = set()
        
        res = set()
        for i in range(len(nums)):
            
            if nums[i] + k in h:
                #if (nums[i]-k, nums[i]) not in res:
                res.add((nums[i],nums[i] + k))
            if nums[i] - k in h:
            #    if nums[i] != k and (nums[i], nums[i]-k) not in res:
                    res.add((nums[i]-k,nums[i]))
            
            h.add(nums[i])
        
        #print(res)
        return len(res)
                
            
        
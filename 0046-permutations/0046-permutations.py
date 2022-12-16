class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        r = []
        def backtrack(bitmap,res):
            
            if len(res) == len(nums):
                r.append(res.copy())
                return
     
            for j in range(len(nums)):
                if bitmap & (1 << j) == 0:
                    res.append(nums[j])
                    backtrack(bitmap | (1 << j),res)
                    res.pop()
            
            
            return r
        
        return backtrack(0,[])
        
        
            
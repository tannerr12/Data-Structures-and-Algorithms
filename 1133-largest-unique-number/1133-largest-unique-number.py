class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        mp = Counter(nums)
        best = -1
        
        for key,val in mp.items():
            if val == 1:
                best = max(best,key)
                
            
        
        return best
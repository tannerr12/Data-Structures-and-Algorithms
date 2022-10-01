class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        
        h = Counter(nums)
        
        for x,y in h.items():
            
            if y == 1:
                return x
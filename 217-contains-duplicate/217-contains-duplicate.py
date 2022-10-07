class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = Counter(nums)
        
        for val in h.values():
            if val > 1:
                return True
            
        
        
        return False
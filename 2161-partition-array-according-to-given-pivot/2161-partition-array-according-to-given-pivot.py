class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        less = []
        equal = []
        great = []
        
        
        for i,v in enumerate(nums):
            
            if v < pivot:
                less.append(v)
            elif v > pivot:
                great.append(v)
            else:
                equal.append(v)
        
        
        return less + equal + great
        
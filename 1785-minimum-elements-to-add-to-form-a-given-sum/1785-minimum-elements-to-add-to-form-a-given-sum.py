class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        
        total = sum(nums)
        
        if total == goal:
            return 0
        
    
        dist = abs(goal - total)
        res = math.ceil(dist / limit)

        
        return res
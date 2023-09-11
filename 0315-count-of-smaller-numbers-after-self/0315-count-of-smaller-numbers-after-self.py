from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sl = SortedList()
        
        ans = [0] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            sl.add(nums[i])
            idx = bisect_left(sl, nums[i])
            
            ans[i] = idx
            
        
        
        return ans
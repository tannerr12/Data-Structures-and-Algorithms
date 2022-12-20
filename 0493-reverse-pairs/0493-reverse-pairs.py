from sortedcontainers import SortedList
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        #2,4,4,6,2
        #1,2,2,3,1
        l = SortedList(key =lambda x : -x)
        res = 0
        
        for i in range(len(nums)):
            
            res+= l.bisect_left(nums[i]*2)
            
            l.add(nums[i])
        
        
        return res
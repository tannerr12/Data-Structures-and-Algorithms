from sortedcontainers import SortedList
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        mp = {}
        sl = SortedList()
        l = 0
        res = 0
        for i in range(len(nums)):
            sl.add(nums[i])
            
            while sl[-1] - sl[0] > 2:
                sl.remove(nums[l])
                l+=1
            
        #    print(len(sl))
            res += len(sl) 
        
       # while sl:
       #     sl.remove(nums[l])
       #     l+=1
       #     res += len(sl) 
        return res
            
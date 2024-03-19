from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        sl = SortedList()
        ans = []
        l = 0
        for i in range(len(nums)):
            
            sl.add(nums[i])
            
            if len(sl) < k:
                continue
            
            if k % 2:
                ans.append(sl[len(sl) // 2])
            else:
                ans.append((sl[len(sl) // 2] + sl[len(sl) // 2 -1]) / 2)
                
            sl.remove(nums[l])
            l+=1
        
        return ans
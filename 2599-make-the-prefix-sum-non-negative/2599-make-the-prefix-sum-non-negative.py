class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        
        count = 0
        idx = 0
        moved = 0
        heap = []
        while idx < len(nums):
            
            count = count + nums[idx]
            heappush(heap,nums[idx])
            if count < 0:
                val = heappop(heap)
                count -= val
                nums.append(val)
                idx +=1
                moved +=1
            else:
                idx +=1
        
        return moved
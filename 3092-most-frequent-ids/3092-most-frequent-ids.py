class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        
        
        ans = [0] * len(nums)
        #heap = []
        #for val in set(nums):
        #    heappush(heap, (0, val))
        arr = [0] * len(nums)
        apply = defaultdict(int)
        
        
        for i in range(len(nums)):
            num = nums[i]
            fr = freq[i]
            idx = bisect_left(arr, apply[num])
            arr.pop(idx)
            apply[num] += fr
            insort(arr, apply[num])
            
            
            ans[i] = arr[-1]
            
            
        
        return ans
            
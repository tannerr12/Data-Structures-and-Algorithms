class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        
        
        ans = [0] * len(nums)
        heap = []
        #for val in set(nums):
        #    heappush(heap, (0, val))
        arr = [0] * len(nums)
        apply = defaultdict(int)
        
        
        for i in range(len(nums)):
            num = nums[i]
            fr = freq[i]
            apply[num] += fr
            heappush(heap, (-apply[num], num))
            
            while heap and -heap[0][0] != apply[heap[0][1]]:
                heappop(heap)
            
            
            ans[i] = -heap[0][0]
            
            
        
        return ans
            
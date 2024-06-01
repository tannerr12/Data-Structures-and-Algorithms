class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        bestr = defaultdict(int)
        #bestl = defaultdict(int)
        
        for i in range(len(nums)-2,-1,-1):
            bestr[i] = max(bestr[i+1], nums[i+1])
        #for i in range(1, len(nums)):
        #    bestl[i] = max(bestl[i-1], nums[i-1])
            
            
        res = float('-inf')
        arr = []
        for i in range(len(nums)):
              
            idx = bisect_right(arr, nums[i]-1)
            idx -= 1
            if bestr[i] > nums[i] and idx < len(arr) and idx >= 0:
                res = max(res, arr[idx] - nums[i] + bestr[i])
            insort(arr, nums[i])
            
        return res
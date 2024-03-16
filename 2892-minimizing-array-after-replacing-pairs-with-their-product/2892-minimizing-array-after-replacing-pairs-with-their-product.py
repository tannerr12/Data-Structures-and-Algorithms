class Solution:
    def minArrayLength(self, nums: List[int], k: int) -> int:
        
        if 0 in nums:
            return 1
        
        d = deque(nums)
        
        ans = 0
        
        
        while len(d) > 1:
            
            first = d.popleft()
            second = d[0]
            
            if first * second <= k:
                d.popleft()
                d.appendleft(first * second)
            else:
                ans += 1
        
        return ans + len(d)
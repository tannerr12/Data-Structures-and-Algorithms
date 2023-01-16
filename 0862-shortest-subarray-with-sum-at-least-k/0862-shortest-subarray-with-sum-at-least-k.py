class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q = deque([[0,0]])
        cur = 0
        res = float('inf')
        for i in range(len(nums)):
            cur += nums[i]
        
            while q and cur - q[0][1] >= k:
                res = min(res,i+1 - q.popleft()[0])
            
            while q and cur <= q[-1][1]:
                q.pop()
            
            q.append([i+1,cur])
            
        
        return res if res != float('inf') else -1
                
            
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        mod = defaultdict(int)
        arr = []
        right = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                right+= grid[i][j]
                arr.append(grid[i][j])
                mod[grid[i][j] % x] += grid[i][j]
                
        if len(mod) > 1:
            return -1
        arr.sort()
        res = float('inf')
        left = 0
        idx = 0
        cur = grid[i][j] % x
        while idx < len(arr):
            
            while cur <= arr[idx]:
                l = ((cur * idx) - (left)) // x
                r = (right - (cur * (len(arr) - idx))) // x
                res = min(res, l + r)
                cur += x
            
            left += arr[idx]
            right -= arr[idx]
            idx +=1
            
        return res
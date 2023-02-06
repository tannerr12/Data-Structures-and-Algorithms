class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        r = n-1
        curr = 0
        prefix = [0] * len(arr)
        minSeen = float('inf')
        res = float('inf')
        for i in range(len(arr)-1,-1,-1):
            
            curr += arr[i]
            while curr > target:
                curr -= arr[r]
                r -=1
            
            if curr == target:
                if r + 1 < len(arr) and prefix and prefix[r+1] != 0:
                    res = min(res, r-i+1 + prefix[r+1])
                minSeen = min(minSeen, r-i+1)
            
            prefix[i] = minSeen if minSeen != float('inf') else 0
            
        
        
        return res if res != float('inf') else -1
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        l = n-1
        curr = 0
        ls = []
        prefix = [0] * len(arr)
        minSeen = float('inf')
        res = float('inf')
        for i in range(len(arr)-1,-1,-1):
            
            curr += arr[i]
            while curr > target:
                curr -= arr[l]
                l -=1
            
            if curr == target:
                ls.append([i, l- i +1])
                if l + 1 < len(arr) and prefix and prefix[l+1] != 0:
                    res = min(res, l-i+1 + prefix[l+1])
                minSeen = min(minSeen, ls[-1][1])
            
            prefix[i] = minSeen if minSeen != float('inf') else 0
            
        
        
        return res if res != float('inf') else -1
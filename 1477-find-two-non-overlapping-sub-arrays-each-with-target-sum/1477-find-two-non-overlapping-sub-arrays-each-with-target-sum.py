class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        l = n-1
        
        curr = 0
        ls = []
        prefix = [0] * len(arr)
        minSeen = float('inf')
        for i in range(len(arr)-1,-1,-1):
            
            curr += arr[i]
            while curr > target:
                curr -= arr[l]
                l -=1
            
            
            if curr == target:
                ls.append([i, l- i +1])
                minSeen = min(minSeen, ls[-1][1])
            
            prefix[i] = minSeen if minSeen != float('inf') else 0
            
        
        
        """
        prefix = []
        p = ls.copy()
        for i in range(len(arr) -1, -1, -1):
            if p and i == p[-1][0]:
                idx, val = p.pop()
                if not prefix:
                    prefix.append(val)
                else:
                    if prefix[-1] != 0:
                        prefix.append(min(val, prefix[-1]))
                    else:
                        prefix.append(val)
                
            else:
                
                if prefix:
                    prefix.append(prefix[-1])
                else:
                    prefix.append(0)
        
        
        
        """
      #  print(ls)
       # print(prefix)
        res = float('inf')
        for x,y in ls:
            if x + y >= len(arr) or prefix[x + y] == 0:
                continue
            res = min(res, y + prefix[x + y])
        
        return res if res != float('inf') else -1
            
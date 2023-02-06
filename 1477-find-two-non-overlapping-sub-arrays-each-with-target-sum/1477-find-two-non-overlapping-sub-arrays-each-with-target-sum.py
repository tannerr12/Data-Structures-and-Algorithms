class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        
        l = 0
        
        curr = 0
        ls = []
        
        for i in range(len(arr)):
            
            curr += arr[i]
            
            while curr > target:
                curr -= arr[l]
                l +=1
            
            
            if curr == target:
                ls.append([l, i - l +1])
                
        
        
        
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
        
        
        prefix.reverse()
        
        res = float('inf')
        #print(ls)
        #print(prefix)
        for x,y in ls:
            if x + y >= len(arr) or prefix[x + y] == 0:
                continue
            res = min(res, y + prefix[x + y])
        
        return res if res != float('inf') else -1
            
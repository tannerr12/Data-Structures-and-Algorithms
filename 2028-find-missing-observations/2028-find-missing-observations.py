class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        target = (len(rolls) + n) * mean
        
        #print(target)
        
        leftover = target - sum(rolls)
        
        mid = leftover // n
        
        #print(leftover)
        
        #print(mid)
        
        if leftover / n > 6 or leftover / n < 1:
            return []
        
        ans = []
        
        while n:
            
            ans.append(mid)
            leftover -= mid
            n -=1
        
        idx = len(ans) -1
        while leftover:
            diff = 6 - ans[idx]
            ans[idx] += min(diff, leftover)
            leftover -= min(diff, leftover)
            idx -=1
        
        
            
        return ans
            
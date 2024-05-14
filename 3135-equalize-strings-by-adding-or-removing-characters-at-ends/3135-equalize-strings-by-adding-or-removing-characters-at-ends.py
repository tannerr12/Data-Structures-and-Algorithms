class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        
        def isGood(mid):
            s = set()
            for i in range(len(target)-mid+1):
                s.add(target[i:i+mid])
            
            for i in range(len(initial)-mid+1):
                if initial[i:i+mid] in s:
                    return True
            
            return False
                
        l, r = 1, len(target)
        res = 0
        while l <= r:
            
            mid = (l+r) // 2
            
            if isGood(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return len(initial) + len(target) - (res * 2)
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        #s = sum(batteries)
        right = sum(batteries[-n:])
        left = sum(batteries[:n-1])
        #print(right)
        #print(left)
        #v = sum(batteries)
        def isGood(val):

            target = val * n
            right = 0
            for i in range(len(batteries) - n, len(batteries)):
                right += min(batteries[i], val)
            s = 0
            for i in range(len(batteries) - n):
                
                s+= min(batteries[i], val)
            
            
            return s + right >= target
            
            
                
        
        
        
        l,r = 0, 10**15
        res = 0
        while l <= r:
            
            mid= (l+r)//2
            
            if isGood(mid):
                res = mid
                l = mid +1
            else:
                r = mid -1
                
        return res
        
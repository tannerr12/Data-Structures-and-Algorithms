class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        total = sum(cost)
        
        tc = []
        
        for x,y in zip(nums,cost):
            tc.append((x,y))
        
        pref = []
        tc.sort()
        for i in range(len(tc)):
            t,c = tc[i]
            if i == 0:
                pref.append(c)
            else:
                pref.append(c + pref[-1])
        
            
        
        #print(tc)
        
        left = [0] * len(tc)
        ltot = 0
        ln = 0
        for i in range(1,len(tc)):
            n,c = tc[i]
            calc = (left[i-1] + (pref[i-1] * (n - tc[i-1][0])))
            left[i] = calc
            ltot += c
            ln += n
        
        right = [0] * len(tc)
        res = float('inf')
        for i in range(len(tc)-2,-1,-1):
            n,c = tc[i]
            calc = (right[i+1] + ((pref[-1] - pref[i]) * (tc[i+1][0] - n)))
            right[i] = calc
            ltot += c
            ln += n
        
        
        
        for x,y in zip(left,right):
            
            res = min(res, x + y)
        
        return res
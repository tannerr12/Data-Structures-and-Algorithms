class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        ls= []
        
        for i in range(len(ranges)):
            ls.append((i - ranges[i],i + ranges[i]))
            
        ls.sort()
        
        idx = 0
        close = 0
        mx = 0
        cost = 0
        
        for i in range(n):
            
            while idx < len(ls) and ls[idx][0] <= i:
                mx = max(mx, ls[idx][1])
                idx +=1

            if i == close:
                if mx <= i:
                    return -1
                close = mx
                cost += 1
                mx = 0
            
        return cost
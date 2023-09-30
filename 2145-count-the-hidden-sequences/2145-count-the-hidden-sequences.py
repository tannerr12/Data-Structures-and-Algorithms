class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
        #1,2,-1,3 = highest = 3 = lowest = -1 
        
        
        #+ 2 lowest = 1 + 2 highest = 5 
        
        #res = upper - highest = 2
        
        
        h,l = lower,lower
        start = lower
        for i in range(len(differences)):
            start += differences[i]
            h = max(h, start)
            l = min(l, start)
        
        
        #print(h)
        #print(l)
        
        
        diff = (lower - l)
        
        h += diff
        
        return max(0,upper - h + 1)
        
        
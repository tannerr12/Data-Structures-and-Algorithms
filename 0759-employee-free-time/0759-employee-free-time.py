"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        inter = []
        
        for i in range(len(schedule)):
            for c in range(len(schedule[i])):
                inter.append([schedule[i][c].start, schedule[i][c].end])
        
        

        
        inter.sort()
        inter.append([float('inf'),float('inf')])
        res = []
        i = 0
        while i < len(inter)-1:
            
            fs,fe = inter[i]
            
            
            while i < len(inter) -1 and fe >= inter[i+1][0]:
                i+=1
                fe = max(inter[i][1], fe)
                
            
            if inter[i+1][0] != float('inf'):
                v = Interval(fe, inter[i+1][0]) 
                res.append(v)
            i+=1
        
        #print(res)
        return res
            
            
            
            
            
            
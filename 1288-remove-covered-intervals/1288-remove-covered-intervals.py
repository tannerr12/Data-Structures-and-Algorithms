class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ignore = 0
        for i in range(len(intervals)):
            a,b = intervals[i]
            for j in range(len(intervals)):
                if i == j:
                    continue
                x,y = intervals[j]
                if x <= a and y >= b:
                    ignore += 1
                    break
        
        return len(intervals) - ignore
                
            
            
            
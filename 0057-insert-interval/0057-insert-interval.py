class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = []
        if len(intervals) == 0:
            stack.append(newInterval)
            return stack
        newx,newy = newInterval
        i = 0
        while i <= len(intervals) -1:
            if (intervals[i][0] <= newx and intervals[i][1] <=newy and newx <= intervals[i][1]) or (newx < intervals[i][0] and newy > intervals[i][0]) or (newy >= intervals[i][0] and newy <= intervals[i][1]):
                
                holdx = intervals[i][0]
                while(i <= len(intervals) -1 and intervals[i][0] <=newy):
                    #++ the iteration in the list
                    i+=1
                #append original x and current Y
                i-=1
                stack.append([min(holdx, newx), max(intervals[i][1], newy)])
                    
            elif i ==0 and newy < intervals[i][0] or intervals[i-1][1] < newx and intervals[i][0] > newy:
                stack.append([newx,newy])
                stack.append([intervals[i][0],intervals[i][1]])
            else:
                stack.append([intervals[i][0],intervals[i][1]])
            i+=1
        
        if newx > intervals[len(intervals) -1][1]:
            stack.append(newInterval)
        return stack
            
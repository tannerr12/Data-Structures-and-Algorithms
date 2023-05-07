from sortedcontainers import SortedList
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        

        ls = []
        res = []
        
        
        for i in range(len(obstacles)):
            v = obstacles[i]
            pos = bisect_right(ls, v)
            
            if pos == len(ls):
                ls.append(v)
            else:
                ls[pos] = v
                
            res.append(pos + 1) 
            
            
        
        
        return res
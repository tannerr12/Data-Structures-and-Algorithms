
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        
        
        #3, 2, 1, 2, 3
        #4, 3, 2, 3, 4
        
        #1,2,2,3,3
        #2,3,3,4,4
        #2,1,3,0,4
        
        
        #1,2,2,3,3
        #2,3,3,4,4
        #2,1,3,0,4
        
        
        
        #[-1,-1,2,-1,-1]
        
        for i in range(len(intervals)):
            intervals[i] = [intervals[i][0], intervals[i][1], i]
        intervals.sort()
        
        heap = []
        ans = [-1] * len(intervals)
        for i in range(len(intervals)):
            x,y,j = intervals[i]
            heappush(heap, (y, j))
            while heap and x >= heap[0][0]:
                val, idx = heappop(heap)
                ans[idx] = j
        
        
        return ans
            
                
            
            
        
            
        
        
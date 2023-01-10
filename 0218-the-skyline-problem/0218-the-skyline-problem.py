from sortedcontainers import SortedList

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        sl = SortedList([0])       
        arr = []
         
        #buildings = sorted(buildings, key=lambda x: (x[0], x[1], x[2]))
        for x,y,z in buildings:
            
            arr.append([x,-z,0])
            arr.append([y,z,1])
            

        
        arr.sort()
        points = []
        for i in range(len(arr)):
            
            
            height = arr[i][1]
            v = arr[i][2]
            x = arr[i][0]
            if v:
                sl.remove(height)
            else:
                sl.add(-height)
                
            
            if not points or points[-1][1] != sl[-1]:
                points.append([x, sl[-1]])
                
        

                
    
        
        return points
            
            

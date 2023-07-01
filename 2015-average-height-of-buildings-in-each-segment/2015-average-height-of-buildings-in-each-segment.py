class Solution:
    def averageHeightOfBuildings(self, buildings: List[List[int]]) -> List[List[int]]:
        
        
        arr = []
        ans = []
        for s,e,h in buildings:
            arr.append((s,h,1))
            arr.append((e, h, -1))
            
        
        arr.sort()
        count = 0
        last = 0
        height = 0
        idx = 0
        overlap = False
        while idx < len(arr):

            pos,h,val = arr[idx]
            h = h * val


            if count > 0 and last != pos:
                if len(ans) > 0 and height // count == ans[-1][2] and overlap:
                    x,y,z = ans.pop()
                    last = x
                ans.append([last, pos, height // count])
                overlap = True
            
            height += h
            count += val
            if count == 0:
                overlap = False
            
            last = pos
            idx +=1
        
        
        return ans
                
            
            
            
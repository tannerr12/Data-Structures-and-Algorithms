class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        
        line = []
        
        for i in range(len(segments)):
            
            start,end, value = segments[i]
            
            line.append((start,value, end))
            line.append((end,-value, start))
        
        ans = []
        
        line.sort()
        #print(line)
        idx = 0
        last = line[idx][0]
        count = 0
        while idx < len(line):
            
            v = line[idx][0]
            
            
            
            while idx < len(line) and line[idx][0] == v:
                if last != line[idx][0]:
                    if count > 0:
                        ans.append([last, line[idx][0], count])
                    last = line[idx][0] 
                count += line[idx][1]
                idx +=1
                
            #print(count)    
        
        #print(ans)
        return ans    
            
class Solution:
    def seePeople(self, heights: List[List[int]]) -> List[List[int]]:
        
        
        #stack =[]
        
        res = [[0 for i in range(len(heights[0]))] for j in range(len(heights))]
        
        
        
        
        for r in range(len(heights)):
            stack =[]
            for c in range(len(heights[0]) - 1, -1, -1):
                
                
                    equal = False
                    
                    while stack and stack[-1] <= heights[r][c]:
                        if stack[-1] == heights[r][c]:
                            equal = True # edge case [[4,2,1,1,3]]
                        stack.pop()
                        res[r][c] +=1 
                        
                    
                        
                    if stack and not equal:
                        res[r][c] +=1
                    stack.append(heights[r][c])
                    
                    
        
        for j in range(len(heights[0])):
            stack = []
            for i in range(len(heights) -1, -1, -1):
                equal = False
                while stack and stack[-1] <= heights[i][j]:
                    if stack[-1] == heights[i][j]:
                        equal = True
                    
                
                    stack.pop()
                    res[i][j] +=1
                
                if stack and not equal:
                    res[i][j] +=1
                stack.append(heights[i][j])
        
   
        
        return res
                
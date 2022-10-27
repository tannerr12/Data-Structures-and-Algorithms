class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        
        img2h = {}
        img1h = {}
        
        
        for r in range(len(img1)):
            
            for c in range(len(img1[0])):
                if img1[r][c] == 1:
                    img1h[(r,c)] = 1
                    
                
        
        
        for r in range(len(img1)):
            
            for c in range(len(img1[0])):
                if img2[r][c] == 1:
                    img2h[(r,c)] = 1
                    
        
        memo = {}
        
        res = 0
        def backtrack(r,c):
            
            nonlocal res
            
            if (r,c) in memo or r <= -len(img1) or c >= len(img1[0]) or r >= len(img1) or c <= -len(img1[0]):
                return 
            tres = 0
            
            
            for x,y in img1h:
                
                if (x + r, c + y) in img2h:
                    tres +=1
                
            
            memo[(r,c)] = tres
            res = max(res,tres)
            
            #check 4 directions
            
            backtrack(r+1,c)
            backtrack(r-1,c)
            backtrack(r,c+1)
            backtrack(r,c-1)
        
        
        
        backtrack(0,0)
        
        return res
            
            
            
            
            
            
                    
                    
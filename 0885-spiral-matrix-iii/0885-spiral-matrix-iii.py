class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        ans = []
        ans.append([rStart,cStart])
        seen = rows * cols
        seen -=1
        moves = 0
        posr, posc = rStart, cStart
        
        
        def intable(r,c):
            nonlocal seen
            if r < rows and c < cols and r >= 0 and c >= 0:
                seen -= 1
                return True
            return False
        
        
        while seen:
            moves += 1
            #move right
            for i in range(moves):
                posc += 1
                if intable(posr,posc):
                    ans.append([posr,posc])
                    
            
            #move down
            for i in range(moves):
                posr += 1
                if intable(posr,posc):
                    ans.append([posr,posc])
            
            moves += 1
            #move left
            for i in range(moves):
                posc -= 1
                if intable(posr,posc):
                    ans.append([posr,posc])
            
            #move up
            for i in range(moves):
                posr -= 1
                if intable(posr,posc):
                    ans.append([posr,posc])
            
            
        
        
        return ans
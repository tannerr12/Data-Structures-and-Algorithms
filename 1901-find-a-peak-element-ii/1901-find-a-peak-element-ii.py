class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        def binaryS(l,r):
            
            while l <= r:
                
                maxRow = 0
                midCol = (l+r) //2
                
                for row in range(len(mat)):
                    maxRow = row if (mat[row][midCol] > mat[maxRow][midCol]) else maxRow
                
                
                leftBig = False
                rightBig = False
                if oob(maxRow, midCol-1) > oob(maxRow,midCol):
                    leftBig = True
                
                if oob(maxRow, midCol+1) > oob(maxRow,midCol):
                    rightBig = True
                
                if(not leftBig) and (not rightBig):
                    return [maxRow, midCol]
                elif rightBig:
                    l = midCol + 1
                else:
                    r = midCol - 1
                
            return []
            
        
        
        def oob(i,j):
            
            if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]):
                return -1
            
            return mat[i][j]
        
        
        return binaryS(0,len(mat[0])-1)
            
        
        
        
        
        
        
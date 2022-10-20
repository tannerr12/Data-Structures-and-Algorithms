class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        def binarySearchLeft(x,y):
            
            l,r = y,len(matrix[0]) -1
            
            while l <= r:
                
                curr = (l+r) // 2
                
                
                if matrix[x][curr] == target:
                    return True
                
                if matrix[x][curr] > target:
                    r = curr -1
                else:
                    l = curr +1
            return False
        
        def binarySearchUp(x,y):
            
            l,r = y,len(matrix) -1
            
            while l <= r:
                
                curr = (l+r) // 2
                
                
                if matrix[curr][y] == target:
                    return True
                
                if matrix[curr][y] > target:
                    r = curr -1
                else:
                    l = curr +1
            return False
        
        for i in range(min(len(matrix), len(matrix[0]))):
            
            if binarySearchLeft(i,i):
                return True
            if binarySearchUp(i,i):
                return True
        
        return False
                
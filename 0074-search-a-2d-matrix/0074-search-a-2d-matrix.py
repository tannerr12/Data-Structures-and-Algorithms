class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearch(row):
            
            l = 0
            r = len(matrix[0]) -1
            
            
            while l <= r:
                
                curr = (l+r)//2
                
                if matrix[row][curr] == target:
                    return True
                elif matrix[row][curr] > target:
                    r = curr -1
                else:
                    l = curr +1
            
            return False
        
        
        
        for r in range(len(matrix)):
            if matrix[r][0] <= target and matrix[r][len(matrix[0]) -1] >= target:
                 return binarySearch(r)
        
        
        return False
                
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #divide and conquer method to search grid
        
        
        def search(left,up,right,down):
            
            
            if left > right or up > down:
                return False
            
            
            #we should check the top left and bottom right corner to make sure target is within range
            elif matrix[up][left] > target or matrix[down][right] < target:
                return False
            
            mid = (left + right) // 2
            
            row = up
            
            while row <= down and matrix[row][mid] <= target:
                
                if matrix[row][mid] == target:
                    return True
                row +=1
            #search bottom left or search top right
            res = search(left,row, mid - 1,down) or search(mid+1, up, right, row-1)
            return res
            
        
        return search(0,0,len(matrix[0])-1, len(matrix)-1)
    
class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m,n = len(matrix), len(matrix[0])
        
        maskArr = [0] * m
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    maskArr[i] |= (1 << n-j-1)
        
        comb = 2 ** (max(m,n)+1)
        #print(comb)
        def  countSetBits(n):
            count = 0
            while (n):
                count += n & 1
                n >>= 1
            return count
        
        #def backtrack(bitmask):
            
           # if i >= m:
           #     return countSetBits(bitmask)
            
        res = 0

        for i in range(comb+1):

            if countSetBits(i) == numSelect:
                temp = 0
                for val in maskArr:
                    if val & i == val:
                        temp +=1

                res = max(res,temp)

        return res

                    
                    
            
        
        
            
        
        
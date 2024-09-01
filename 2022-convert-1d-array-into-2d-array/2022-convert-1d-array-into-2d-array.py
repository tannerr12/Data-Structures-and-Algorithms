class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        arr = [[0 for j in range(n) ] for i in range(m)]
        count = 0
        print(arr)
        for i in range(m):
            
            for j in range(n):
                arr[i][j] = original[count]
                count += 1
            
        
        
        return arr
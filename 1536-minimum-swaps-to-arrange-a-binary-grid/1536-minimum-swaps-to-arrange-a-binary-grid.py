class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        numbers = []
        
        for i in range(n):
            count = 0
            for j in range(n-1,-1,-1):
                if grid[i][j] != 0:
                    break
                
                count += 1
            
            numbers.append(count)
            
        def swap(i,j):
            ans = 0
            while j != i:
                numbers[j-1], numbers[j] = numbers[j], numbers[j-1]
                j-=1
                ans += 1
            
            return ans 
        res = 0
        while True:
            need = -1
            found = False
            for i in range(len(numbers)):
                if numbers[i] < n - 1 - i and need == -1:
                    need = n-1-i
            
                if numbers[i] >= need and need != -1:
                    res += swap(n - need - 1, i)
                    need = -1
                    found = True
                    break
            
            if need != -1:
                return -1
            if not found:
                break
        
        return res
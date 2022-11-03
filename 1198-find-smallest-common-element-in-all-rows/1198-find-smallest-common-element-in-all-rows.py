class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        
        h = defaultdict(int)
        res = float('inf')
        
        
        for r in range(len(mat)):
            
            for c in range(len(mat[r])):
                
                h[mat[r][c]] +=1
                if h[mat[r][c]] == len(mat):
                    res = min(res,mat[r][c])
        
        
        
        
        return res if res != float('inf') else -1
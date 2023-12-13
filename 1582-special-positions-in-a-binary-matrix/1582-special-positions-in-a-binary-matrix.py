class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        seen = defaultdict(int)
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    seen[('r' + str(i))] += 1
                    seen[('c' + str(j))] += 1
                    
        
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and seen['r' + str(i)] == 1 and seen['c' + str(j)] == 1:
                    res += 1
        return res
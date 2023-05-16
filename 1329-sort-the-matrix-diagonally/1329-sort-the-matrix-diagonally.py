class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        def oob(i,j):
            
            if i >= len(mat) or i < 0 or j >= len(mat[0]) or j < 0:
                return False
            
            return True
            
        mp = defaultdict(list)
        for i in range(len(mat)):
            
            if i == 0:
                for j in range(len(mat[0])):
                    a,b = i,j
                    
                    while oob(a,b):
                        mp[(i,j)].append(mat[a][b])
                        a+=1
                        b+=1
                    
                    mp[(i,j)].sort()
                    
                    a,b = i,j
                    idx = 0
                    while oob(a,b):
                        mat[a][b] = mp[(i,j)][idx]
                        a+=1
                        b+=1
                        idx +=1
            
            else:
                
                a,b = i,0
                
                while oob(a,b):
                    mp[(i,0)].append(mat[a][b])
                    a+=1
                    b+=1

                mp[(i,0)].sort()
                
                a,b = i,0
                idx = 0
                while oob(a,b):
                    mat[a][b] = mp[(i,0)][idx]
                    a+=1
                    b+=1
                    idx +=1
        
        
        return mat
                
            
            
            
            
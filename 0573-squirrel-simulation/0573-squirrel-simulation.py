class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], sq: List[int], nuts: List[List[int]]) -> int:
        #maximum tree distance minimum sq distance
        res = 0
        NutTree = float('-inf')
        sNut = 0
        treeMax = 0
        
        pairs = []
        for x,y in nuts:
            res += (abs(x - tree[0]) + abs(y - tree[1])) * 2
            pairs.append(((abs(x - tree[0]) + abs(y - tree[1])), (abs(x - sq[0]) + abs(y - sq[1]))))
            
            if (abs(x - tree[0]) + abs(y - tree[1])) - (abs(x - sq[0]) + abs(y - sq[1])) > NutTree:
          
                sNut = (abs(x - sq[0]) + abs(y - sq[1]))
                treeMax = (abs(x - tree[0]) + abs(y - tree[1]))
                NutTree = (abs(x - tree[0]) + abs(y - tree[1])) - (abs(x - sq[0]) + abs(y - sq[1])) 
                
            
            
        return res + sNut - treeMax
            
            
                
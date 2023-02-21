class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        #bitmask + dp needed
       
        #111 [][][]
        #101 [][ ]
        #011 [ ][]
        combinations = []
        
        def findComb(rem,curr):
            
            if rem == 0:
                combinations.append(curr)
                
                return

            for j in range(len(bricks)):
                minus = rem - bricks[j]
            
                if minus >= 0:
                    if minus > 0:
                        findComb(minus,curr | (1 << minus))
                    else:
                        findComb(minus,curr)
        findComb(width,0)
        
        #print(combinations)
                     
        @cache
        def dfs(i,prev):
            
            if i >= height:
                return 1
            
            res = 0
            for j in range(len(combinations)):
                if combinations[j] & prev == 0:
                    res += dfs(i+1,combinations[j])
                
            
            return res
        
        
        return dfs(0,0) % (10 ** 9 +7)
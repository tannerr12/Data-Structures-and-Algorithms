class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        
        width = sum(wall[0])
      #  print(width)
        
        dp = collections.defaultdict(int)
        #h = wall[0][0]
        #l = len(wall[0])
        #allSame = True
        #print(dp)
        
        #edge = 0
        for r in range(len(wall)):
            rsum = 0
            for c in range(len(wall[r])):
                
                #if wall[r][0] != h or len(wall[r]) != l:
                 #   allSame = False
                    
                
                rsum+=wall[r][c]
                if rsum != width:
                    dp[rsum] += 1
        
        
        #print(dp)
        
        return len(wall) - max(dp.values()) if len(dp.values()) > 0 else len(wall)
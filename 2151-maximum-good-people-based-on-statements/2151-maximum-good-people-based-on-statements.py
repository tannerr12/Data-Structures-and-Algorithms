class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        
        
        def dfs(i, good, bad):
            
            if i >= len(statements):
                return 0
            
            res = float('-inf')
            #try each person good or bad
            #if good all statements must line up
            #if someone is good all statements should be recorded
            bgood = good
            bbad = bad
            for j in range(len(statements[i])):
                canbegood=True
                if statements[i][j] == 0 and good & (1 << j) > 0:
                    canbegood = False
                    break
                elif statements[i][j] == 1 and bad & (1 << j) > 0:
                    canbegood = False
                    break
                elif statements[i][j] == 0:
                    bbad |= (1 << j)
                elif statements[i][j] == 1:
                    bgood |= (1 << j)
            
            #already good
            if good & (1 << i) > 0 and canbegood == False:
                return float('-inf')
            elif canbegood and bad & (1 << i) == 0:
                res = max(res, dfs(i+1, bgood | (1 << i), bbad) + 1)
            
            if good & (1 << i) == 0:
                res = max(res, dfs(i+1, good, bad | (1 << i)))
        
                      
            return res
            
            
        
                      
        return dfs(0, 0, 0)
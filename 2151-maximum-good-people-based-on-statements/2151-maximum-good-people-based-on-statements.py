class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        
        maskGood = defaultdict(int)
        maskBad = defaultdict(int)
        
        for i in range(len(statements)):
            for j in range(len(statements[i])):
                if statements[i][j] == 0:
                    maskBad[i] |= (1 << j)
                if statements[i][j] == 1:
                    maskGood[i] |= (1 << j)
        
        
        def dfs(i, good, bad):
            
            if i >= len(statements):
                return 0
            
            res = float('-inf')
            #try each person good or bad
            #if good all statements must line up
            #if someone is good all statements should be recorded
            bgood = good 
            bbad = bad
            #take all statements as fact
            bgood |= maskGood[i]
            bbad |= maskBad[i]
            
            #check for conflicting statments
            canbegood = (good & maskBad[i]) == 0 and (bad & maskGood[i]) == 0
            

            #can be good and is not already bad
            if canbegood and bad & (1 << i) == 0:
                #take statments as fact
                res = max(res, dfs(i+1, bgood | (1 << i), bbad) + 1)
            
            #can be bad and is not already good
            if good & (1 << i) == 0:
                #no statements updated
                res = max(res, dfs(i+1, good, bad | (1 << i)))
        
                      
            return res
            
                      
        return dfs(0, 0, 0)
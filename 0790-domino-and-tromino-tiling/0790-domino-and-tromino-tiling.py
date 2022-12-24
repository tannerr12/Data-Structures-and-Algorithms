class Solution:
    def numTilings(self, n: int) -> int:
        
        
        @cache
        def dfs(i,state1,state2):
            
            if i >= n:
                return 1
            
            state3, state4 = True, True
            if i == n-1:
                state3 = False
                state4 = False
            
            res = 0
            if state1 and state2:
                #vertical
                res += dfs(i+1,True,True)
                if state3:
                    #L shape top right
                    res += dfs(i+1, False, True)
                if state4:
                    #L shape bottom right
                    res += dfs(i+1, True, False)
                if state3 and state4:
                    res += dfs(i+1, False,False)
            
            if state1 and not state2:
                if state3:
                    #flat top
                    res += dfs(i+1, False,True)
                if state3 and state4:
                    #L shape top left
                    res += dfs(i+1,False,False)
            
            if not state1 and state2:
                if state4:
                    #flat bottom
                    res += dfs(i+1,True,False)
                if state3 and state4:
                    # l shape bottom right
                    res += dfs(i+1, False,False)
            
            
            if not state1 and not state2:
                res += dfs(i+1, state3, state4)
            
            
            
            return res
        
        
        res = dfs(0,True, True)
        return res % (10 ** 9 + 7)
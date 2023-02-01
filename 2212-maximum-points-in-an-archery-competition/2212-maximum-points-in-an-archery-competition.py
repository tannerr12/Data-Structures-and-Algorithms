class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        
        
        res = [0] * len(aliceArrows)
        
        final = [0,[0]]
        
        @cache
        def dfs(i,left,total):
            nonlocal res
            nonlocal final
            if i < 0 or left ==0:
                
                if total > final[0]:
                    final = [total, res.copy()]
                
                return
                    
            
            #take
            if aliceArrows[i] +1 <= left and i != 0:
                val = res[i]
                res[i] = aliceArrows[i] + 1
                dfs(i-1, left - (aliceArrows[i] + 1), total + i)
                res[i] = val
            
            elif i == 0:
                val = res[0]
                res[0] = left
                dfs(i-1,0,total)
                res[0] = val
            
            if i != 0:
                #dont take
                dfs(i-1,left,total)
            

        dfs(len(aliceArrows) -1,numArrows,0)
        
        #print(final)
        return final[1]
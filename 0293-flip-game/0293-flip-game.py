class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        
        res = []
        
        
        for i in range(len(currentState) -1):
            
            if currentState[i] == '+' and currentState[i+1] == '+':
                temp = currentState[0:i] + '--' + currentState[i+2:]
                res.append(temp)
        
        
        return res
        
        
        def dfs(i,currS):
            
            
            if i >= len(currentState):
                res.append(currS)
            
            
            
            
            
            #win flip
            if currentState[i] == '+' and currentState[i+1] == '+':
                
                
                return 0
            
            
            #lose Flip
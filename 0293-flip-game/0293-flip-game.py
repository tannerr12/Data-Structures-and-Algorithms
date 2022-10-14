class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        
        res = []
        
        
        for i in range(len(currentState) -1):
            
            if currentState[i] == '+' and currentState[i+1] == '+':
                temp = currentState[0:i] + '--' + currentState[i+2:]
                res.append(temp)
        
        
        return res
        
        

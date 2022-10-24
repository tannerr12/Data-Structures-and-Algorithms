class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        choice = [i for i in range(1,maxChoosableInteger+1)]
       
        totalSum = (maxChoosableInteger+1 ) * maxChoosableInteger / 2
        
        if totalSum < desiredTotal:
            return False
        
        if totalSum == desiredTotal:
            return maxChoosableInteger % 2
        
        memo = {}
        def dfs(choice, remain):
            
         
            if choice[-1] >= remain:
                return True
            
            if tuple(choice) in memo:
                return memo[tuple(choice)]
            
            
            for i in range(len(choice)):                    
            
                if not dfs(choice[:i] + choice[i+1:],remain-choice[i]):
                    memo[tuple(choice)] = True
                    return True    
                
                
            
            memo[tuple(choice)] = False
            return False
                    
        
        
        return dfs(choice,desiredTotal)
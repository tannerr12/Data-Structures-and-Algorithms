class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        
        s = set()
        
        @cache
        def dfs(i):
            
            if i > primeOne * primeTwo:
                return 0 
            
            s.add(i)
            
            #add p1
            dfs(i + primeOne)
            #add p2
            dfs(i + primeTwo)
            
            
        
        dfs(0)
        
        for i in range(primeOne * primeTwo -1, 0, -1):
            if i not in s:
                return i
        
            
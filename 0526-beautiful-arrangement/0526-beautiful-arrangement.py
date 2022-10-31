class Solution:
    def countArrangement(self, n: int) -> int:
        print(n)
        
        #1, 2, 3 ,4, 5, 6
        #1, 2 ,3 ,8, 10, 36
        
        count = 0 
        memo = defaultdict(int)
        def backtrack(pos):
            nonlocal count
            if pos > n:
                count+=1
            
            for i in range(1,n+1):
                if memo[i] == False and (i % pos == 0 or pos % i == 0):
                    memo[i] = True
                    backtrack(pos+1)
                    memo[i] = False
                    
        
        
        backtrack(1)
        return count
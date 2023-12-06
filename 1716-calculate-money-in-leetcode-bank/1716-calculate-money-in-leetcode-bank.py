class Solution:
    def totalMoney(self, n: int) -> int:
        
        def count(i,j):
            return ((i + j) * (j - i + 1)) //2
        

        week = 1
        total = 0
    
        while 7 * week <= n:
            total += count(week, week+6)
            week += 1
        
        total += count(week, week + (n-((week-1) * 7)-1))
        
        return total


            
            
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        two,three,five = 0,0,0
        
        
        res = [1]
        
        while len(res) < n:
            
            while res[two] * 2 <= res[-1]: two+=1
            while res[three] * 3 <= res[-1]: three+=1
            while res[five] * 5 <= res[-1]: five+=1
            
            res.append(min(res[two] * 2, res[three] * 3, res[five] * 5))
            
        
        
        return res[n-1]
                
        
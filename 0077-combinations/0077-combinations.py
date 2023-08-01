class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        temp = []
        def comb(i):
            
            if i > n or len(temp) == k:
                if len(temp) == k:
                    res.append(temp.copy())
                return
            
            #take 
            temp.append(i)
            comb(i+1)
            temp.pop()
            #dont take
            comb(i+1)
        
        
        comb(1)
        
        return res
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        h = Counter(tasks)
        res = 0
        for key,val in h.items():
            if val < 2:
                return -1
            x = val / 3
            
            if x % 1 == 0:
                res += int(x)
            else:
                res += val // 3 + 1
        return res
                        
                
                
            
            
                
            
            
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        h = Counter(tasks)
        res = 0
        for key,val in h.items():
            if val < 2:
                return -1
            if val % 3 == 0:
                res += val // 3
            else:
                res += val // 3 + 1
        return res
                        
                
                
            
            
                
            
            
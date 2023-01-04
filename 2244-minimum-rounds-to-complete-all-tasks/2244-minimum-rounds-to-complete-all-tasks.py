class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        #tasks.sort()
        h = Counter(tasks)
        
        res = 0
        for key,val in h.items():
            if val < 2:
                return -1
            x = val / 3
            
            if x % 1 == 0:
                res += int(x)
            else:
                l = 0
                while val > 0:
                    if val % 3 != 0:
                        val -=2
                        l +=1
                    
                    else:
                        l+= val // 3
                        break
                res +=l
        
        return res
                        
                
                
            
            
                
            
            
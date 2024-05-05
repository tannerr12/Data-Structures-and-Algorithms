class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        
        consec = []
        count = 0
        for val in road:
            
            if val == 'x':
                count += 1
            else:
                if count > 0:
                    consec.append(count)
                count = 0
            
        
        if count > 0:
            consec.append(count)
            
        
        consec.sort(reverse=True)
        
        res = 0
        for val in consec:
            
            if budget >= val + 1:
                res += val
                budget -= (val+1)
            else:
                res += budget - 1
                budget = 0
                
            
            if budget == 0:
                break
        return res
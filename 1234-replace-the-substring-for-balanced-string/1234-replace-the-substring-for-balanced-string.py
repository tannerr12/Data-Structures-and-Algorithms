class Solution:
    def balancedString(self, s: str) -> int:
        
        #idea 1 - not used
        # find gap from all letters away from target
        #sliding window that can close the gap
        #keep counts of sliding window total - sliding = res
        full = Counter(s)
        target = len(s) /4
    

        res = float('inf')

        l= 0
        for i in range(len(s)):
                    
            full[s[i]] -=1
                    
            while l < len(s) and all(target >= full[c] for c in 'QWER'):
                res = min(res, i-l + 1)
                full[s[l]] +=1
                
                l+=1
       

        return res
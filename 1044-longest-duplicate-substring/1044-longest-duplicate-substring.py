class Solution:
    def longestDupSubstring(self, s: str) -> str:
        
        def isGood(mid):
           
            st = set()
            for j in range(len(s)):

                if s[j:j+mid] in st:
                    return s[j:j+mid]

                st.add(s[j:j+mid])
                
            return ''
    
        l,r = 1, len(s)
        res = ''
        while l <= r:
            
            mid = (l + r) // 2    
            val = isGood(mid)
            
            if val != '':
                res = val
                l = mid + 1
            else:
                r = mid -1
        
        
        
        
        return res
    
        
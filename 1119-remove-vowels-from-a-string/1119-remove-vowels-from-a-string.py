class Solution:
    def removeVowels(self, s: str) -> str:
        v = ['a', 'e', 'i', 'o', 'u']
        
        st = []
        
        for val in s:
            if val not in v:
                st.append(val)
                
        
        return ''.join(st)
        
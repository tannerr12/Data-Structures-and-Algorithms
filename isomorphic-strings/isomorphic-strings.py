class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        mapping = {}
        mappingT = {}
        for i in range(len(s)):
            if (s[i] in mapping and mapping[s[i]] != t[i]) or t[i] in mappingT and mappingT[t[i]] != s[i]:
                return False
            mapping[s[i]] = t[i]
            mappingT[t[i]] = s[i]
        
    
        return True
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        
        
        mp = {}
        taken = set()
        def dfs(i,c):
            
            if i >= len(s) and c >= len(pattern):
                return True
            elif i >= len(s):
                return False
            elif c >= len(pattern):
                return False
            
            
            res = False
            char = pattern[c]
            if char in mp:
                #v = s[i:i + len(mp[char])]
                #vv = mp[char]
                if s[i:i + len(mp[char])] != mp[char]:
                    return False
                else:
                    res = res or dfs(i + len(mp[char]), c + 1)
            else:
                
                for j in range(i, len(s)):
                    st = s[i:j+1]
                    
                    if st in taken:
                        continue
                    mp[char] = st
                    taken.add(st)
                    res = res or dfs(j + 1, c + 1)
                    del mp[char]
                    taken.remove(st)
            
            
            return res
        
        
        return dfs(0,0)
                    
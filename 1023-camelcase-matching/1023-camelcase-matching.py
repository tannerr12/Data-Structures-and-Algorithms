class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        ans = []
        
        mp = defaultdict(Counter)
        patt = []
        s = ''
        for i in range(len(pattern)):
            
            if pattern[i].isupper():
                if len(s) > 0:
                    mp[s] = Counter(s)
                    patt.append(s)
                s = ''
            s += pattern[i]
            
        if len(s) > 0:
            mp[s] = Counter(s)
            patt.append(s)
        
        for i in range(len(queries)):
            md = defaultdict(Counter)
            s = ''
            idx = 0
            p = []
            for j in range(len(queries[i])):

                if queries[i][j].isupper():
                    if len(s) > 0:
                        md[idx] = Counter(s)
                        idx +=1
                        p.append(s)
                    s = ''
                s += queries[i][j]
                
            if len(s) > 0:
                md[idx] = Counter(s)
                p.append(s)
            idx = 0
            if pattern[0].isupper() and queries[i][0].islower():
                idx +=1
            if len(p)-idx != len(patt):
                ans.append(False)
                continue
            
            for k in patt:
                fail = False
                for key,val in mp[k].items():
                    if idx not in md or md[idx][key] < val:
                        fail = True
                        break
                if fail:
                    break
                idx+=1
                
            if fail:
                ans.append(False)
            else:
                ans.append(True)
            
                
        
        return ans
                
            
            
            
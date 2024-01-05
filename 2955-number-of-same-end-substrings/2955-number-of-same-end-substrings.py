class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        
        #for i in range(len(queries)):
        #    queries[i].append(i)
            
        #queries.sort()
        
        
        l = 0
        mp = defaultdict(lambda: defaultdict(int))
        
        
        for i in range(len(s)):
            if i == 0:
                mp[i][s[i]] += 1
            
            else:
                for key,val in mp[i-1].items():
                    mp[i][key] += val
                
                mp[i][s[i]] += 1
        
        #print(mp)
                
        res = []
        
        for x,y in queries:
            
            total = 0
            for key,val in mp[y].items():
                v = val - mp[x-1][key]
                total += (v * (v + 1)) // 2
            
            res.append(total)
            
        return res
            
            
            
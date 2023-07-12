class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        
        mp = defaultdict(dict)
        
        tot = defaultdict(int)
        
        for i in range(len(s)):
            
            tot[s[i]] += 1
            mp[i] = tot.copy()
        
        
        ans = [False] * len(queries)
        
        for i in range(len(queries)):
            r = mp[queries[i][1]]
            l = mp[queries[i][0]]
            diff = defaultdict(int)
            k = queries[i][2]
            size = 0
            for j in range(26):
                letter = chr(ord('a') + j) 
                diff[letter] = r[letter] - l[letter]
                size += diff[letter]
            diff[s[queries[i][0]]] += 1
            size +=1
            
            extra = 0
            for key,val in diff.items():
                if val % 2:
                    extra += 1
            
            if (extra - (extra % 2)) // 2 <= k:
                ans[i] = True
        
        
        return ans
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        
        mp = defaultdict(list)
        for j, (x,y) in enumerate(queries):
            
            lf = []
            seen1 = False
            for i in range(30,-1,-1):
                
                has1 = x & (1 << i)
                has2 = y & (1 << i)
                
                if has1 and has2 and seen1:
                    lf.append('0')
                
                elif not has1 and not has2 and seen1:
                    lf.append('0')
                
                elif (has1 and not has2) or (has2 and not has1):
                    seen1 = True
                    lf.append('1')
                    
            
            st = ''.join(lf)
            if st == '':
                st = '0'
            mp[st].append(j)
            #print(st)
        
        
        #print(mp)
        
        ans = [[-1,-1]] * len(queries)
        for i in range(30):
            
            for j in range(i, len(s)):
                
                if s[j-i:j+1] in mp:
                    while mp[s[j-i:j+1]]:
                        idx = mp[s[j-i:j+1]].pop()
                        ans[idx] = [j-i, j]
                    del mp[s[j-i:j+1]]
        
        return ans
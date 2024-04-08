class Solution:
    def maxSubstringLength(self, s: str) -> int:
        
        #all that matters is first and last postions of any character
        #prefix sum 
        
        c = Counter(s)
        fl = defaultdict(lambda:[float('inf'),-1])
        prefix = [[0 for i in range(26)] for j in range(len(s) + 1)]
        
        #N * 26
        for i in range(len(s)):
            ch = s[i]
            chv = ord(ch) - ord('a')
            for j in range(len(prefix[i])):
                prefix[i+1][j] = prefix[i][j]
            
            prefix[i+1][chv] += 1
            fl[ch][0] = min(fl[ch][0], i)
            fl[ch][1] = max(fl[ch][1], i)
            
        
        starts = []
        ends = []
        
        #26
        for key,val in fl.items():
            starts.append(val[0])
            ends.append(val[1])
            
        #(26 * log(26))
        starts.sort()
        ends.sort(reverse=True)
        res = 0
        
        #26 * 26 * 26
        for i in range(len(starts)):
            for j in range(len(ends)):
                if starts[i] > ends[j]:
                    break
                elif (starts[i] == 0 and ends[j] == len(s) -1):
                    continue
                    
                valid = True
                for k in range(26):
                    e = prefix[ends[j] + 1][k]
                    st = prefix[starts[i]][k]
                    n = e - st
                    char = chr(k + ord('a'))
                    
                    if n != 0 and n != c[char]:
                        valid = False
                        break
                    
                if valid:
                    res = max(res, ends[j] - starts[i] + 1)
                    break
                    
        
        
        return res if res > 0 else -1
                
                
        
        

        
        
        
        
            
            
            
            
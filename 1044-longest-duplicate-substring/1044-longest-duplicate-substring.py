class Solution:
    def longestDupSubstring(self, s: str) -> str:
        MOD = 9223372036854775807
        
        def check(num, word,st):
            
            for pos in st[num]:
                if s[pos - mid: pos + 1] == word:
                    return True
            
            return False
        
        def isGood(mid):
            st = defaultdict(list)
            val = 0
            
            for j in range(len(s)):
                if j < mid:
                    val = (val + ((ord(s[j]) - ord('a') + 1) * pow(26, (mid - j -1),MOD))) % MOD
                    if j+1 < mid: 
                        continue
                else:
                    val = (val - ((ord(s[j-mid]) - ord('a') + 1) * pow(26,(mid - 1),MOD))) % MOD
                    val = (val * 26) % MOD
                    val = (val + ((ord(s[j]) - ord('a') + 1) * pow(26, 0, MOD))) % MOD
                
                if val in st:
                    if check(val, s[j-mid:j+1],st):
                        return s[j-mid:j+1]

                st[val].append(j)
                
            return ''
    
        l,r = 0, len(s)
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
    
        
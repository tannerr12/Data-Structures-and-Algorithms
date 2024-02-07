class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        
        als = []
        bls = []
        
        for i in range(len(s)):
            
            if s[i:i+len(a)] == a:
                als.append(i)
            if s[i:i+len(b)] == b:
                bls.append(i)
        
        ans = []
        
        for i in range(len(als)):
            
            idx = bisect_right(bls, als[i])
            idx -= 1
            if idx >= 0 and abs(bls[idx] - als[i]) <= k:
                ans.append(als[i])
                continue
                
            idx += 1
            if idx < len(bls):
                if abs(bls[idx] - als[i]) <= k:
                    ans.append(als[i])
                    continue
        
        return ans
                
            
            
            
        
            
        
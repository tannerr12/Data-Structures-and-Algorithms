class Solution:
    def beautySum(self, s: str) -> int:
        
        res = 0
        for i in range(len(s)):
            count = defaultdict(int)
            count[s[i]] = 1
            for j in range(i+1,len(s)):
                count[s[j]] +=1
                if len(count) > 1:
                    res += abs(max(count.values()) - min(count.values()))
                    
        
        return res
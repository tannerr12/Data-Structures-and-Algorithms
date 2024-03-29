class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        total = [0] * len(words)
        for i in range(len(words)):
            
            c = Counter(words[i])
            mn = min(c)
            total[i] = c[mn]
        
        
        
        total.sort()
        
        ans = []
        for i in range(len(queries)):
            c = Counter(queries[i])
            mn = min(c)
            count = c[mn]
        
            idx = bisect_right(total, count)
            
            ans.append(len(total) - idx)
        
        
        return ans
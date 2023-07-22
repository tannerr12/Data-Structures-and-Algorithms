class Solution:
    def minNumberOfFrogs(self, cr: str) -> int:
        c = Counter()
        prev = {'r': 'c', 'o': 'r', 'a': 'o', 'k': 'a'}
        res = 0
        for let in cr:
            
            if let != 'c':
                
                if c[prev[let]] <= c[let]:
                    return -1
            
            c[let] += 1
            
            if let == 'k':
                for key in c:
                    c[key] -=1
            res = max(res,max(c.values()))

        return res if max(c.values()) == 0 else -1
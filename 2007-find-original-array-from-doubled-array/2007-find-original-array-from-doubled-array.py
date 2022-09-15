class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        if len(changed) % 2:
            return []
        h = Counter(changed)
        seen = 0
        res = []
        for i in range(len(changed)):
            if changed[i] in h:
                if h[changed[i]] <= 0:
                    continue
            if changed[i] * 2 in h:
                if h[changed[i] *2] <=0:
                    continue
            if changed[i] in h and changed[i] *2 in h:
                if changed[i] == 0 and h[changed[i]] < 2:
                    continue
                h[changed[i]] -=1
                h[changed[i] *2] -=1
                res.append(changed[i])
                seen +=2
         
            
            if seen == len(changed):
                break
        
        
        return res if len(res) == len(changed) //2 else []
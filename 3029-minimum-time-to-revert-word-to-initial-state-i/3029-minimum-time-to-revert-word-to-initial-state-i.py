class Solution:
    def minimumTimeToInitialState(self, s: str, k: int) -> int:
        

        n = len(s)
        z = [0] * n
        l, r = 0, 0

        for i in range(1, n):
            if i < r:
                z[i] = min(r - i, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] > r:
                l = i
                r = i + z[i]

        
        count = 1
        best = 0
        for i in range(len(z)-1,-1,-1):
        
            if i % k == 0 and z[i] == count:
                best = math.ceil((len(z) - count) / k)
            
            count += 1
        
        worst = math.ceil(len(s) / k)
        return worst if best == 0 else best
            
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
    
        h = defaultdict(int)
        res = 0
        for i in range(len(time)):
            time[i] %= 60
            target = 60 - time[i] 
            res += h[target]
            
            if target == 60:
                h[60] += 1
            h[time[i]] += 1
        
        return res
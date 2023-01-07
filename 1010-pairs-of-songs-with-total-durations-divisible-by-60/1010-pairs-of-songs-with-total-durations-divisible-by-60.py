class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        for i in range(len(time)):
            time[i] %= 60
        h = defaultdict(int)
        res = 0
        for i in range(len(time)):
            
            target = 60 - time[i] 
            #target2 = 60 - time[i]
            if target in h:
                res += h[target]
            
           # if target2 in h and target != target2:
           #     res +=1
            
            if target == 60:
                h[60] += 1
            h[time[i]] += 1
        
        return res
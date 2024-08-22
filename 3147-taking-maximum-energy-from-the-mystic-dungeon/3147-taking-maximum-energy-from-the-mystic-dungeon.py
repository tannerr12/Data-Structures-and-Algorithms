class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        
        mod = defaultdict(int)
        res = float('-inf')
        for i in range(len(energy)-1,-1,-1):
            
            mod[i%k] += energy[i]
            res = max(res,mod[i%k])
        
        
        return res
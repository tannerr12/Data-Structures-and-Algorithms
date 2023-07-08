class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        res = 1
        seen = set()
        
        for i in range(len(rolls)):
            
            seen.add(rolls[i])
            
            if len(seen) == k:
                res +=1
                seen = set()
        
        return res
        
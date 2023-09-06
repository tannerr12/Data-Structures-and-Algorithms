class Solution:
    def findMinMoves(self, machines: List[int]) -> int:

        total = sum(machines)
        
        if total % len(machines) != 0:
            return -1

        target = total // len(machines)
        

        
        res = 0
        diff = 0
    
        for i in range(len(machines)):
            diff += machines[i] - target
            res = max(res, abs(diff))
            res = max(res, machines[i] - target)
          
        return res

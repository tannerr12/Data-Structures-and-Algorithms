class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        
     
        res = 0
        total = 0
        totalTank = 0
        for i in range(len(gas)):
               
             
                totalTank += gas[i] - cost[i]
                total += gas[i] - cost[i]
                
                if total < 0:

                    total = 0
                    res = i +1

               
        return res if totalTank >= 0 else -1
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        tasks = sorted(tasks, key=lambda x: (-(x[1] - x[0])))
              
        energy = 0
        energyNeeded = 0
        for x,y in tasks:
            if y > energy:
                diff = y - energy
                energyNeeded += diff
                energy += diff
                
            energy -= x
        
        return energyNeeded

        

        
        
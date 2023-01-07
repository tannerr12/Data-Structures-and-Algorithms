class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        
        tNext = defaultdict(int)
        
        day = 0
        
        for i in range(len(tasks)):
            
            if i == 0 or i + day > tNext[tasks[i]]:
             
                tNext[tasks[i]] = i + day + space
            
            else:
                day += (tNext[tasks[i]] - (i + day)) +1
                tNext[tasks[i]] = i + day + space
                
        
        return len(tasks) + day
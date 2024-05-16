class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        tasks.sort()
        processorTime.sort()
        res = 0
        for i in range(len(processorTime)):
            cur = processorTime[i]
            worst = 0
            for i in range(min(4,len(tasks))):
                val = tasks.pop()
                worst = max(worst, cur + val)
            
            res = max(res, worst)
            if len(tasks) == 0:
                break
            #heappush(processorTime, worst)
                
            
            
        return res
        
        
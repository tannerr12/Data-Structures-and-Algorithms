class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        tasks.sort()
        heapify(processorTime)
        res = 0
        while tasks:
            cur = heappop(processorTime)
            worst = 0
            for i in range(min(4,len(tasks))):
                val = tasks.pop()
                worst = max(worst, cur + val)
            
            res = max(res, worst)
            #heappush(processorTime, worst)
                
            
            
        return res
        
        
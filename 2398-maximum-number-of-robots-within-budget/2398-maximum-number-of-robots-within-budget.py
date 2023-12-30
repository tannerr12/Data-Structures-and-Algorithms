class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        heap = []
        res = 0
        l = 0
        score = 0
        for i in range(len(chargeTimes)):
            
            heappush(heap, [-chargeTimes[i], i])
            score += runningCosts[i]
            
            ct = -heap[0][0]
        
            
            while heap and ct + (i - l + 1) * score > budget:
                ct = -heap[0][0]
                score -= runningCosts[l]
                if heap and heap[0][1] < (l+1):
                    heappop(heap)
                l+=1
            
            while heap and heap[0][1] < l:
                heappop(heap)
            
            
            res = max(res, i - l + 1)
                
        
        return res
        
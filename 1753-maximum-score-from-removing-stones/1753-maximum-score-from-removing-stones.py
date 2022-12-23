class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        
        
        heap = []
        heap.append(-a)
        heap.append(-b)
        heap.append(-c)
        
        heapq.heapify(heap)
        zeroes = 0
        score = 0
        
        while heap and zeroes < 2:
            
            val1 = heapq.heappop(heap)
            val2 = heapq.heappop(heap)
            
            if val1 == -1:
                zeroes += 1
            else:
                heappush(heap,(val1 +1))
            if val2 == -1:
                zeroes +=1
            else:
                heappush(heap,(val2 + 1))
                
            
            
            score +=1
        
            
            
            
            
        
        return score
            
            
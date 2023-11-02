class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:

        h = defaultdict(list)
  
        heap = []
        
        for w in range(len(workers)):
            worker = workers[w]
            for b in range(len(bikes)):
                bike = bikes[b]
                manhatten = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                heap.append((manhatten, w, b))
        
        
        heap.sort()
        heapq.heapify(heap)
        seen = set()

      
        answer = [-1] * len(workers)
        while heap and len(seen) != len(workers):
            x,y,z = heapq.heappop(heap)
            if z not in seen and answer[y] == -1:
                answer[y] = z
                seen.add(z)


        return answer
         

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:


        adj = defaultdict(list)
        i = 0
        for fromm,to in edges:
            succ = succProb[i]
            adj[fromm].append((to,succ))
            adj[to].append((fromm,succ))
            i +=1

        
        heap = [(-1,start)]
        seen = set()
        
        while heap:

            weight,node = heapq.heappop(heap)
            weight = -weight 
            if node in seen:
                continue
            seen.add(node)

            if node == end:
                return weight
            
            for n, w in adj[node]:
                if n in seen:
                    continue
                heapq.heappush(heap,((w * weight) * -1, n))
        
        return 0

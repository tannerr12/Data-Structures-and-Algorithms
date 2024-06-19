class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        
        neighbors = defaultdict(set)
        for source, target in corridors:
            neighbors[source].add(target)
            neighbors[target].add(source)
            
        ans = 0
        for firstNode in range(1,n+1):
            for thirdNode in range(firstNode+1,n+1):
                if firstNode in neighbors[thirdNode]:
                    ans += len(neighbors[firstNode].intersection(neighbors[thirdNode]))
        return ans//3
        
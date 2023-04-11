class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        indegreeZ = set([i for i in range(n)])
        for x,y in edges:
            
            if y in indegreeZ:
                indegreeZ.remove(y)
                
        
        return list(indegreeZ)
            
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        adj = defaultdict(list)
        impMap = defaultdict(int)
        for emp in employees:
            x = emp.id
            y = emp.importance
            
            impMap[x] = y
            for val in emp.subordinates:
                adj[x].append(val)
            
        def dfs(i):
            
            if i is None:
                return 0
            
            res = impMap[i]
            for val in adj[i]:
                res += dfs(val)
            
            
            return res
        
        return dfs(id)
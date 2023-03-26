class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        #a cycle node must have atleast 1 indegree and 1 outdegree
        #just keep track of node counts than if we see the same node again take count - count when we saw that node
        
        res = 0
        gseen = set()
        for i in range(len(edges)):
            idx = i
            count = 0
            valid = False
            seen = {}
            while idx not in gseen:
                seen[idx] = count
                idx = edges[idx]
                count +=1
                if idx == -1:
                    break
                if idx in seen:
                    count = count - seen[idx]
                    valid = True
                    break
            if valid:
                gseen |= seen.keys()
                res = max(res,count)
        
        
        return res if res > 0 else -1
from itertools import combinations
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        
        adj = defaultdict(list)
        in_degrees = [0] * n
        if len(relations) == 0:
            return math.ceil(n / k)

        for x,y in relations:

            adj[x-1].append(y-1)
            in_degrees[y-1] +=1
            

        
        @cache
        def recurse(mask,in_degrees):
            
            if not mask:
                return 0
            
            nodes = [i for i in range(n) if mask & 1 << i and in_degrees[i] ==0]
            ans = float('inf')
            for k_nodes in combinations(nodes,min(len(nodes),k)):
                new_mask, new_in_degrees= mask, list(in_degrees)
                for node in k_nodes:
                    new_mask ^= 1 << node
                    for no in adj[node]:
                        new_in_degrees[no] -=1
                        
                    
                ans = min(ans,1 + recurse(new_mask, tuple(new_in_degrees)))
            
            
            
            return ans
        
        return recurse((1 << n) -1, tuple(in_degrees))


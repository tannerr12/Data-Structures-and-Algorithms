class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        adjFlip = defaultdict(list)

        for x,y in edges:

            adj[x].append(y)
            adjFlip[y].append(x)
            

        rootrevs = 0
        ans = [0] * n
        
        def dfs(node, par, depth, revs):
            nonlocal rootrevs
            ans[node] = -revs + (depth - revs)
            #non flips
            for a in adj[node]:
                if a == par:
                    continue
                res = dfs(a, node, depth + 1, revs)

            #flips
            for a in adjFlip[node]:
                if a == par:
                    continue
                rootrevs += 1
                res = dfs(a, node, depth + 1, revs + 1)
        
        dfs(0, None, 0 ,0)
        for i, diff in enumerate(ans):
            ans[i] = diff + rootrevs
        
        return ans
            

      